__kernel void run_add(__read_only image2d_t img_in_bg, __read_only image2d_t img_in_fg, __write_only image2d_t img_out, sampler_t sampler, int out_width, int out_height)
{
	int x = get_global_id(0);
	int y = get_global_id(1);
}
