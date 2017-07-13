# encoding: utf8
from __future__ import division, absolute_import

__copyright__ = "Copyright (C) 2009-16 Andreas Kloeckner"

__license__ = """
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""


# {{{ documentation

__doc__ = u"""
PyOpenCL now includes and uses some of the `Random123 random number generators
<https://www.deshawresearch.com/resources_random123.html>`_ by D.E. Shaw
Research.  In addition to being usable through the convenience functions above,
they are available in any piece of code compiled through PyOpenCL by::

    #include <pyopencl-random123/philox.cl>
    #include <pyopencl-random123/threefry.cl>

See the `Philox source
<https://github.com/pyopencl/pyopencl/blob/master/pyopencl/cl/pyopencl-random123/philox.cl>`_
and the `Threefry source
<https://github.com/pyopencl/pyopencl/blob/master/pyopencl/cl/pyopencl-random123/threefry.cl>`_
for some documentation if you're planning on using Random123 directly.

.. note::

    PyOpenCL previously had documented support for the `RANLUXCL random number
    generator <https://bitbucket.org/ivarun/ranluxcl/>`_ by Ivar Ursin
    Nikolaisen.  This support is now deprecated because of the general slowness
    of these generators and will be removed from PyOpenCL in the 2018.x series.
    All users are encouraged to switch to one of the Random123 genrators,
    :class:`PhiloxGenerator` or :class:`ThreefryGenerator`.

.. autoclass:: PhiloxGenerator

.. autoclass:: ThreefryGenerator

.. autofunction:: rand
.. autofunction:: fill_rand

"""

# }}}

import pyopencl as cl
import pyopencl.array as cl_array
import pyopencl.cltypes as cltypes
from pyopencl.tools import first_arg_dependent_memoize
from pytools import memoize_method

import numpy as np


# {{{ RanluxGenerator (deprecated)

class RanluxGenerator(object):
    """
    .. warning::

        This class is deprecated, to be removed in PyOpenCL 2018.x.

    .. versionadded:: 2011.2

    .. attribute:: state

        A :class:`pyopencl.array.Array` containing the state of the generator.

    .. attribute:: nskip

        nskip is an integer which can (optionally) be defined in the kernel
        code as RANLUXCL_NSKIP. If this is done the generator will be faster
        for luxury setting 0 and 1, or when the p-value is manually set to a
        multiple of 24.
    """

    def __init__(self, queue, num_work_items=None,
            luxury=None, seed=None, no_warmup=False,
            use_legacy_init=False, max_work_items=None):
        """
        :param queue: :class:`pyopencl.CommandQueue`, only used for initialization
        :param luxury: the "luxury value" of the generator, and should be 0-4,
            where 0 is fastest and 4 produces the best numbers. It can also be
            >=24, in which case it directly sets the p-value of RANLUXCL.
        :param num_work_items: is the number of generators to initialize,
            usually corresponding to the number of work-items in the NDRange
            RANLUXCL will be used with.  May be `None`, in which case a default
            value is used.
        :param max_work_items: should reflect the maximum number of work-items
            that will be used on any parallel instance of RANLUXCL. So for
            instance if we are launching 5120 work-items on GPU1 and 10240
            work-items on GPU2, GPU1's RANLUXCLTab would be generated by
            calling ranluxcl_intialization with numWorkitems = 5120 while
            GPU2's RANLUXCLTab would use numWorkitems = 10240. However
            maxWorkitems must be at least 10240 for both GPU1 and GPU2, and it
            must be set to the same value for both. (may be `None`)

        .. versionchanged:: 2013.1
            Added default value for `num_work_items`.
        """

        if luxury is None:
            luxury = 4

        if num_work_items is None:
            if queue.device.type & cl.device_type.CPU:
                num_work_items = 8 * queue.device.max_compute_units
            else:
                num_work_items = 64 * queue.device.max_compute_units

        if seed is None:
            from time import time
            seed = int(time()*1e6) % 2 << 30

        self.context = queue.context
        self.luxury = luxury
        self.num_work_items = num_work_items

        from pyopencl.characterize import has_double_support
        self.support_double = has_double_support(queue.device)

        self.no_warmup = no_warmup
        self.use_legacy_init = use_legacy_init
        self.max_work_items = max_work_items

        src = """
            %(defines)s

            #include <pyopencl-ranluxcl.cl>

            kernel void init_ranlux(unsigned seeds,
                global ranluxcl_state_t *ranluxcltab)
            {
              if (get_global_id(0) < %(num_work_items)d)
                ranluxcl_initialization(seeds, ranluxcltab);
            }
            """ % {
                    "defines": self.generate_settings_defines(),
                    "num_work_items": num_work_items
                }
        prg = cl.Program(queue.context, src).build()

        # {{{ compute work group size

        wg_size = None

        import sys
        import platform
        if ("darwin" in sys.platform
                and "Apple" in queue.device.platform.vendor
                and platform.mac_ver()[0].startswith("10.7")
                and queue.device.type & cl.device_type.CPU):
            wg_size = (1,)

        self.wg_size = wg_size

        # }}}

        self.state = cl_array.empty(queue, (num_work_items, 112), dtype=np.uint8)
        self.state.fill(17)

        prg.init_ranlux(queue, (num_work_items,), self.wg_size, np.uint32(seed),
                self.state.data)

    def generate_settings_defines(self, include_double_pragma=True):
        lines = []
        if include_double_pragma and self.support_double:
            lines.append("""
                #if __OPENCL_C_VERSION__ < 120
                #pragma OPENCL EXTENSION cl_khr_fp64: enable
                #endif
                """)

        lines.append("#define RANLUXCL_LUX %d" % self.luxury)

        if self.no_warmup:
            lines.append("#define RANLUXCL_NO_WARMUP")

        if self.support_double:
            lines.append("#define RANLUXCL_SUPPORT_DOUBLE")

        if self.use_legacy_init:
            lines.append("#define RANLUXCL_USE_LEGACY_INITIALIZATION")

            if self.max_work_items:
                lines.append(
                        "#define RANLUXCL_MAXWORKITEMS %d" % self.max_work_items)

        return "\n".join(lines)

    @memoize_method
    def get_gen_kernel(self, dtype, distribution="uniform"):
        size_multiplier = 1
        arg_dtype = dtype

        if dtype == np.float64:
            bits = 64
            c_type = "double"
            rng_expr = "(shift + scale * gen)"
        elif dtype == np.float32:
            bits = 32
            c_type = "float"
            rng_expr = "(shift + scale * gen)"
        elif dtype == cltypes.float2:
            bits = 32
            c_type = "float"
            rng_expr = "(shift + scale * gen)"
            size_multiplier = 2
            arg_dtype = np.float32
        elif dtype in [cltypes.float3, cltypes.float4]:
            bits = 32
            c_type = "float"
            rng_expr = "(shift + scale * gen)"
            size_multiplier = 4
            arg_dtype = np.float32
        elif dtype == np.int32:
            assert distribution == "uniform"
            bits = 32
            c_type = "int"
            rng_expr = ("(shift "
                    "+ convert_int4((float) scale * gen) "
                    "+ convert_int4(((float) scale / (1<<24)) * gen))")

        elif dtype == np.int64:
            assert distribution == "uniform"
            bits = 64
            c_type = "long"
            rng_expr = ("(shift "
                    "+ convert_long4((float) scale * gen) "
                    "+ convert_long4(((float) scale / (1l<<24)) * gen)"
                    "+ convert_long4(((float) scale / (1l<<48)) * gen)"
                    ")")

        else:
            raise TypeError("unsupported RNG data type '%s'" % dtype)

        rl_flavor = "%d%s" % (bits, {
                "uniform": "",
                "normal": "norm"
                }[distribution])

        src = """//CL//
            %(defines)s

            #include <pyopencl-ranluxcl.cl>

            typedef %(output_t)s output_t;
            typedef %(output_t)s4 output_vec_t;
            #define NUM_WORKITEMS %(num_work_items)d
            #define RANLUX_FUNC ranluxcl%(rlflavor)s
            #define GET_RANDOM_NUM(gen) %(rng_expr)s

            kernel void generate(
                global ranluxcl_state_t *ranluxcltab,
                global output_t *output,
                unsigned long out_size,
                output_t scale,
                output_t shift)
            {

              ranluxcl_state_t ranluxclstate;
              ranluxcl_download_seed(&ranluxclstate, ranluxcltab);

              // output bulk
              unsigned long idx = get_global_id(0)*4;
              while (idx + 4 < out_size)
              {
                  *(global output_vec_t *) (output + idx) =
                      GET_RANDOM_NUM(RANLUX_FUNC(&ranluxclstate));
                  idx += 4*NUM_WORKITEMS;
              }

              // output tail
              output_vec_t tail_ran = GET_RANDOM_NUM(RANLUX_FUNC(&ranluxclstate));
              if (idx < out_size)
                output[idx] = tail_ran.x;
              if (idx+1 < out_size)
                output[idx+1] = tail_ran.y;
              if (idx+2 < out_size)
                output[idx+2] = tail_ran.z;
              if (idx+3 < out_size)
                output[idx+3] = tail_ran.w;

              ranluxcl_upload_seed(&ranluxclstate, ranluxcltab);
            }
            """ % {
                "defines": self.generate_settings_defines(),
                "rlflavor": rl_flavor,
                "output_t": c_type,
                "num_work_items": self.num_work_items,
                "rng_expr": rng_expr
                }

        prg = cl.Program(self.context, src).build()
        knl = prg.generate
        knl.set_scalar_arg_dtypes([None, None, np.uint64, arg_dtype, arg_dtype])

        return knl, size_multiplier

    def fill_uniform(self, ary, a=0, b=1, queue=None):
        """Fill *ary* with uniformly distributed random numbers in the interval
        *(a, b)*, endpoints excluded.

        :return: a :class:`pyopencl.Event`

        .. versionchanged:: 2014.1.1

            Added return value.
        """

        if queue is None:
            queue = ary.queue

        knl, size_multiplier = self.get_gen_kernel(ary.dtype, "uniform")
        return knl(queue,
                (self.num_work_items,), None,
                self.state.data, ary.data, ary.size*size_multiplier,
                b-a, a)

    def uniform(self, *args, **kwargs):
        """Make a new empty array, apply :meth:`fill_uniform` to it.
        """
        a = kwargs.pop("a", 0)
        b = kwargs.pop("b", 1)

        result = cl_array.empty(*args, **kwargs)

        result.add_event(
                self.fill_uniform(result, queue=result.queue, a=a, b=b))
        return result

    def fill_normal(self, ary, mu=0, sigma=1, queue=None):
        """Fill *ary* with normally distributed numbers with mean *mu* and
        standard deviation *sigma*.

        .. versionchanged:: 2014.1.1

            Added return value.
        """

        if queue is None:
            queue = ary.queue

        knl, size_multiplier = self.get_gen_kernel(ary.dtype, "normal")
        return knl(queue,
                (self.num_work_items,), self.wg_size,
                self.state.data, ary.data, ary.size*size_multiplier, sigma, mu)

    def normal(self, *args, **kwargs):
        """Make a new empty array, apply :meth:`fill_normal` to it.
        """
        mu = kwargs.pop("mu", 0)
        sigma = kwargs.pop("sigma", 1)

        result = cl_array.empty(*args, **kwargs)

        result.add_event(
                self.fill_normal(result, queue=result.queue, mu=mu, sigma=sigma))
        return result

    @memoize_method
    def get_sync_kernel(self):
        src = """//CL//
            %(defines)s

            #include <pyopencl-ranluxcl.cl>

            kernel void sync(
                global ranluxcl_state_t *ranluxcltab)
            {
              ranluxcl_state_t ranluxclstate;
              ranluxcl_download_seed(&ranluxclstate, ranluxcltab);
              ranluxcl_synchronize(&ranluxclstate);
              ranluxcl_upload_seed(&ranluxclstate, ranluxcltab);
            }
            """ % {
                "defines": self.generate_settings_defines(),
                }
        prg = cl.Program(self.context, src).build()
        return prg.sync

    def synchronize(self, queue):
        """The generator gets inefficient when different work items invoke the
        generator a differing number of times. This function ensures
        efficiency.
        """

        self.get_sync_kernel()(queue, (self.num_work_items,),
                self.wg_size, self.state.data)

# }}}


# {{{ Random123 generators

class Random123GeneratorBase(object):
    """
    .. versionadded:: 2016.2

    .. automethod:: fill_uniform
    .. automethod:: uniform
    .. automethod:: fill_normal
    .. automethod:: normal
    """

    def __init__(self, context, key=None, counter=None, seed=None):
        int32_info = np.iinfo(np.int32)
        from random import Random

        rng = Random(seed)

        if key is not None and counter is not None and seed is not None:
            raise TypeError("seed is unused and may not be specified "
                    "if both counter and key are given")

        if key is None:
            key = [
                    rng.randrange(
                        int(int32_info.min), int(int32_info.max)+1)
                    for i in range(self.key_length-1)]
        if counter is None:
            counter = [
                    rng.randrange(
                        int(int32_info.min), int(int32_info.max)+1)
                    for i in range(4)]

        self.context = context
        self.key = key
        self.counter = counter

        self.counter_max = int32_info.max

    @memoize_method
    def get_gen_kernel(self, dtype, distribution):
        size_multiplier = 1
        arg_dtype = dtype

        rng_key = (distribution, dtype)

        if rng_key in [("uniform", np.float64), ("normal", np.float64)]:
            c_type = "double"
            scale1_const = "((double) %r)" % (1/2**32)
            scale2_const = "((double) %r)" % (1/2**64)
            if distribution == "normal":
                transform = "box_muller"
            else:
                transform = ""

            rng_expr = (
                    "shift + scale * "
                    "%s( %s * convert_double4(gen)"
                    "+ %s * convert_double4(gen))"
                    % (transform, scale1_const, scale2_const))

            counter_multiplier = 2

        elif rng_key in [(dist, cmp_dtype)
                for dist in ["normal", "uniform"]
                for cmp_dtype in [
                    np.float32,
                    cltypes.float2,
                    cltypes.float3,
                    cltypes.float4,
                    ]]:
            c_type = "float"
            scale_const = "((float) %r)" % (1/2**32)

            if distribution == "normal":
                transform = "box_muller"
            else:
                transform = ""

            rng_expr = (
                    "shift + scale * %s(%s * convert_float4(gen))"
                    % (transform, scale_const))
            counter_multiplier = 1
            arg_dtype = np.float32
            try:
                _, size_multiplier = cltypes.vec_type_to_scalar_and_count[dtype]
            except KeyError:
                pass

        elif rng_key == ("uniform", np.int32):
            c_type = "int"
            rng_expr = (
                    "shift + convert_int4((convert_long4(gen) * scale) / %s)"
                    % (str(2**32)+"l")
                    )
            counter_multiplier = 1

        elif rng_key == ("uniform", np.int64):
            c_type = "long"
            rng_expr = (
                    "shift"
                    "+ convert_long4(gen) * (scale/two32) "
                    "+ ((convert_long4(gen) * scale) / two32)"
                    .replace("two32", (str(2**32)+"l")))
            counter_multiplier = 2

        else:
            raise TypeError(
                    "unsupported RNG distribution/data type combination '%s/%s'"
                    % rng_key)

        kernel_name = "rng_gen_%s_%s" % (self.generator_name, distribution)
        src = """//CL//
            #include <%(header_name)s>

            typedef %(output_t)s output_t;
            typedef %(output_t)s4 output_vec_t;
            typedef %(gen_name)s_ctr_t ctr_t;
            typedef %(gen_name)s_key_t key_t;

            uint4 gen_bits(key_t *key, ctr_t *ctr)
            {
                union {
                    ctr_t ctr_el;
                    uint4 vec_el;
                } u;

                u.ctr_el = %(gen_name)s(*ctr, *key);
                if (++ctr->v[0] == 0)
                    if (++ctr->v[1] == 0)
                        ++ctr->v[2];

                return u.vec_el;
            }

            #if %(include_box_muller)s
            output_vec_t box_muller(output_vec_t x)
            {
                #define BOX_MULLER(I, COMPA, COMPB) \
                    output_t r##I = sqrt(-2*log(x.COMPA)); \
                    output_t c##I; \
                    output_t s##I = sincos((output_t) (2*M_PI) * x.COMPB, &c##I);

                BOX_MULLER(0, x, y);
                BOX_MULLER(1, z, w);
                return (output_vec_t) (r0*c0, r0*s0, r1*c1, r1*s1);
            }
            #endif

            #define GET_RANDOM_NUM(gen) %(rng_expr)s

            kernel void %(kernel_name)s(
                int k1,
                #if %(key_length)s > 2
                int k2, int k3,
                #endif
                int c0, int c1, int c2, int c3,
                global output_t *output,
                long out_size,
                output_t scale,
                output_t shift)
            {
                #if %(key_length)s == 2
                key_t k = {{get_global_id(0), k1}};
                #else
                key_t k = {{get_global_id(0), k1, k2, k3}};
                #endif

                ctr_t c = {{c0, c1, c2, c3}};

                // output bulk
                unsigned long idx = get_global_id(0)*4;
                while (idx + 4 < out_size)
                {
                    *(global output_vec_t *) (output + idx) =
                        GET_RANDOM_NUM(gen_bits(&k, &c));
                    idx += 4*get_global_size(0);
                }

                // output tail
                output_vec_t tail_ran = GET_RANDOM_NUM(gen_bits(&k, &c));
                if (idx < out_size)
                  output[idx] = tail_ran.x;
                if (idx+1 < out_size)
                  output[idx+1] = tail_ran.y;
                if (idx+2 < out_size)
                  output[idx+2] = tail_ran.z;
                if (idx+3 < out_size)
                  output[idx+3] = tail_ran.w;
            }
            """ % {
                "kernel_name": kernel_name,
                "gen_name": self.generator_name,
                "header_name": self.header_name,
                "output_t": c_type,
                "key_length": self.key_length,
                "include_box_muller": int(distribution == "normal"),
                "rng_expr": rng_expr
                }

        prg = cl.Program(self.context, src).build()
        knl = getattr(prg, kernel_name)
        knl.set_scalar_arg_dtypes(
                [np.int32] * (self.key_length - 1 + 4)
                + [None, np.int64, arg_dtype, arg_dtype])

        return knl, counter_multiplier, size_multiplier

    def _fill(self, distribution, ary, scale, shift, queue=None):
        """Fill *ary* with uniformly distributed random numbers in the interval
        *(a, b)*, endpoints excluded.

        :return: a :class:`pyopencl.Event`
        """

        if queue is None:
            queue = ary.queue

        knl, counter_multiplier, size_multiplier = \
                self.get_gen_kernel(ary.dtype, distribution)

        args = self.key + self.counter + [
                ary.data, ary.size*size_multiplier,
                scale, shift]

        n = ary.size
        from pyopencl.array import splay
        gsize, lsize = splay(queue, ary.size)

        evt = knl(queue, gsize, lsize, *args)

        self.counter[0] += n * counter_multiplier
        c1_incr, self.counter[0] = divmod(self.counter[0], self.counter_max)
        if c1_incr:
            self.counter[1] += c1_incr
            c2_incr, self.counter[1] = divmod(self.counter[1], self.counter_max)
            self.counter[2] += c2_incr

        return evt

    def fill_uniform(self, ary, a=0, b=1, queue=None):
        return self._fill("uniform", ary,
                scale=(b-a), shift=a, queue=queue)

    def uniform(self, *args, **kwargs):
        """Make a new empty array, apply :meth:`fill_uniform` to it.
        """
        a = kwargs.pop("a", 0)
        b = kwargs.pop("b", 1)

        result = cl_array.empty(*args, **kwargs)

        result.add_event(
                self.fill_uniform(result, queue=result.queue, a=a, b=b))
        return result

    def fill_normal(self, ary, mu=0, sigma=1, queue=None):
        """Fill *ary* with normally distributed numbers with mean *mu* and
        standard deviation *sigma*.
        """

        return self._fill("normal", ary, scale=sigma, shift=mu, queue=queue)

    def normal(self, *args, **kwargs):
        """Make a new empty array, apply :meth:`fill_normal` to it.
        """
        mu = kwargs.pop("mu", 0)
        sigma = kwargs.pop("sigma", 1)

        result = cl_array.empty(*args, **kwargs)

        result.add_event(
                self.fill_normal(result, queue=result.queue, mu=mu, sigma=sigma))
        return result


class PhiloxGenerator(Random123GeneratorBase):
    __doc__ = Random123GeneratorBase.__doc__

    header_name = "pyopencl-random123/philox.cl"
    generator_name = "philox4x32"
    key_length = 2


class ThreefryGenerator(Random123GeneratorBase):
    __doc__ = Random123GeneratorBase.__doc__

    header_name = "pyopencl-random123/threefry.cl"
    generator_name = "threefry4x32"
    key_length = 4

# }}}


@first_arg_dependent_memoize
def _get_generator(context):
    if context.devices[0].type & cl.device_type.CPU:
        gen = PhiloxGenerator(context)
    else:
        gen = ThreefryGenerator(context)

    return gen


def fill_rand(result, queue=None, luxury=None, a=0, b=1):
    """Fill *result* with random values of `dtype` in the range [0,1).
    """
    if luxury is not None:
        from warnings import warn
        warn("Specifying the 'luxury' argument is deprecated and will stop being "
                "supported in PyOpenCL 2018.x", stacklevel=2)

    if queue is None:
        queue = result.queue
    gen = _get_generator(queue.context)
    gen.fill_uniform(result, a=a, b=b)


def rand(queue, shape, dtype, luxury=None, a=0, b=1):
    """Return an array of `shape` filled with random values of `dtype`
    in the range [a,b).
    """

    if luxury is not None:
        from warnings import warn
        warn("Specifying the 'luxury' argument is deprecated and will stop being "
                "supported in PyOpenCL 2018.x", stacklevel=2)

    from pyopencl.array import Array
    gen = _get_generator(queue.context)
    result = Array(queue, shape, dtype)
    result.add_event(
            gen.fill_uniform(result, a=a, b=b))
    return result


# vim: filetype=pyopencl:foldmethod=marker
