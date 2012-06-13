__kernel void run_add(__read_only image2d_t img_in_bg, __read_only image2d_t img_in_fg, __write_only image2d_t img_out, sampler_t sampler, int out_width, int out_height)
{
	int x = get_global_id(0);
	int y = get_global_id(1);
	
	float2 coord = (float2)((float)x / (float)out_width, (float)y / (float)out_height);
	if(x < out_width){
		if(y < out_height){
			float4 bg = read_imagef(img_in_bg, sampler, coord);
			float4 fg = read_imagef(img_in_fg, sampler, coord);
			write_imagef(img_out, (int2)(x, y), fg + bg);
		}
	}
}
