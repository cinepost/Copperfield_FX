__constant sampler_t sampler = CLK_NORMALIZED_COORDS_FALSE | CLK_ADDRESS_CLAMP_TO_EDGE | CLK_FILTER_NEAREST;

__kernel void quantize_show( __read_only image2d_t img_in, __write_only image2d_t img_out){ 
    int x = get_global_id(0);
	int y = get_global_id(1);
	float4 in = read_imagef(img_in, sampler, (int2)(x, y));
	in = clamp(in, (float4)(0.0f, 0.0f, 0.0f, 0.0f), (float4)(1.0f, 1.0f, 1.0f, 1.0f));
	write_imagef(img_out, (int2)(x, y), in * 255.0f);
}
