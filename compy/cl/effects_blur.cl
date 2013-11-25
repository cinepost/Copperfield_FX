__constant sampler_t sampler = CLK_NORMALIZED_COORDS_TRUE | CLK_ADDRESS_CLAMP_TO_EDGE | CLK_FILTER_LINEAR;

__kernel void fast_blur_h(
        __read_only image2d_t image_in,
        __write_only image2d_t image_out,
        float blur_diameter, float blur_diametery, int img_width, int img_height, int indepy)
      {

    int x = get_global_id(0);
	int y = get_global_id(1);

	float2 coord = (float2)((float)x / (float)img_width, (float)y / (float)img_height);
    
	int x_samples = img_width * blur_diameter + 2;
	float dx = blur_diameter / x_samples;
	
	float4 sum = 0.f;
	float ww = 0.f;
	float dist = 0.f;
	float2 sample_coord;
	float w;
	for(int a = 0; a < x_samples; a++){
		sample_coord = coord;
		dist = a * dx - blur_diameter / 2.f;
		sample_coord.x += dist;
		w = 1.f - fabs(dist / (blur_diameter / 2.f));
		ww += w;
		sum += read_imagef(image_in, sampler, sample_coord) * w;
	}


    sum /= ww;
    write_imagef(image_out, (int2)(x, y), sum);
}

__kernel void fast_blur_v(
        __read_only image2d_t image_in,
        __write_only image2d_t image_out,
        float blur_diameter, float blur_diametery, int img_width, int img_height, int indepy)
      {

    int x = get_global_id(0);
	int y = get_global_id(1);

	float2 coord = (float2)((float)x / (float)img_width, (float)y / (float)img_height);
    
	int y_samples = img_height * blur_diametery + 2;
	float dy = blur_diametery / y_samples;
	
	float4 sum = 0.f;
	float ww = 0.f;
	float dist = 0.f;
	float2 sample_coord;
	float w;
	for(int a = 0; a < y_samples; a++){
		sample_coord = coord;
		dist = a * dy - blur_diametery / 2.f;
		sample_coord.y += dist;
		w = 1.f - fabs(dist / (blur_diametery / 2.f));
		ww += w;
		sum += read_imagef(image_in, sampler, sample_coord) * w;
	}


    sum /= ww;
    float4 zero = 0.f;
    float4 one = 1.f;
    sum = clamp(sum, zero, one);
    write_imagef(image_out, (int2)(x, y), sum);
}
