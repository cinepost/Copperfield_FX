__constant sampler_t sampler = CLK_NORMALIZED_COORDS_TRUE | CLK_ADDRESS_CLAMP_TO_EDGE | CLK_FILTER_LINEAR;

__kernel void test(void){
	float4 val = 1.0f;
}

__kernel void run_jpg(	__read_only image2d_t img_in_r,
						__read_only image2d_t img_in_g,
						__read_only image2d_t img_in_b, __write_only image2d_t img_out, int in_width, int in_height, int out_width, int out_height)
{
	int x = get_global_id(0);
	int y = get_global_id(1);

	float2 coord = (float2)((float)x / (float)out_width, (float)y / (float)out_height);
	float4 val = 1.0f;

		val.x = read_imagef(img_in_r, sampler, coord).x;
		val.y = read_imagef(img_in_g, sampler, coord).x;
		val.z = read_imagef(img_in_b, sampler, coord).x;
		write_imagef(img_out, (int2)(x, y), val);
		//write_imagef(img_out, (int2)(x, y), float4(0.75f, 0.5f, 0.25f, 0.0f));

}


__kernel void run_exr(	__read_only image2d_t img_in_r,
						__read_only image2d_t img_in_g,
						__read_only image2d_t img_in_b,
						__read_only image2d_t img_in_a, __write_only image2d_t img_out, int in_width, int in_height, int out_width, int out_height)
{
	int x = get_global_id(0);
	int y = get_global_id(1);

	float2 coord = (float2)((float)x / (float)out_width, (float)y / (float)out_height);
	if(x < out_width){
		if(y < out_height){
			float4 val = 1.0f;
			val.x = read_imagef(img_in_r, sampler, coord).x;
			val.y = read_imagef(img_in_g, sampler, coord).x;
			val.z = read_imagef(img_in_b, sampler, coord).x;
			val.w = read_imagef(img_in_a, sampler, coord).x;
			write_imagef(img_out, (int2)(x, y), val);
		}
	}
}