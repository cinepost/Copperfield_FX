CL_TRACE = False
CL_ENABLE_GL = False
CL_USE_SHIPPED_EXT = True
CL_INC_DIR = []
CL_LIB_DIR = []
CL_LIBNAME = []
CXXFLAGS = ['-std=gnu++11', '-stdlib=libc++', '-mmacosx-version-min=10.7', '-arch', 'i386', '-arch', 'x86_64']
LDFLAGS = ['-std=gnu++11', '-stdlib=libc++', '-mmacosx-version-min=10.7', '-arch', 'i386', '-arch', 'x86_64', '-Wl,-framework,OpenCL']
