__constant sampler_t sampler = CLK_NORMALIZED_COORDS_FALSE | CLK_ADDRESS_CLAMP_TO_EDGE | CLK_FILTER_LINEAR;

__kernel void fast_blur_h(
        __read_only image2d_t image_in,
        __write_only image2d_t image_out,
        float blur_diameter, int img_width, int img_height)
      {

	int x = get_global_id(0);
	int y = get_global_id(1);
	float2 sample_coord = (float2)(x + .5f, y + .5f);

	float4 sum = read_imagef(image_in, sampler, sample_coord); // central pixel of a blur kernel

    if(blur_diameter > 0.0f) {
    	float blur_radius_in_pixels = img_width * (blur_diameter / 2.0);
		int side_samples = floor(blur_radius_in_pixels); // half number of full samples, e.g. for a blur diameter 5.2 pixels side_samples would be 2.

		float total_weights = 1.f; // the weight of a central sample
		float sample_weight;

		// sampling left and right side_samples
		for(int i = 1; i <= side_samples; i++){
			sample_weight = (side_samples - i) / blur_radius_in_pixels;
			total_weights += sample_weight * 2;
			sum += read_imagef(image_in, sampler, sample_coord + (float2)(i, 0)) * sample_weight;
			sum += read_imagef(image_in, sampler, sample_coord - (float2)(i, 0)) * sample_weight;
		}

    	sum /= total_weights;
    	write_imagef(image_out, (int2)(x, y), sum);
	
	}
	write_imagef(image_out, (int2)(x, y), sum);
}

__kernel void fast_blur_v(
        __read_only image2d_t image_in,
        __write_only image2d_t image_out,
        float blur_diameter, int img_width, int img_height)
      {

    int x = get_global_id(0);
	int y = get_global_id(1);
	float2 sample_coord = (float2)(x + .5f, y + .5f);
    
	float4 sum = read_imagef(image_in, sampler, sample_coord); // central pixel of a blur kernel

    if(blur_diameter > 0.0f) {
    	float blur_radius_in_pixels = img_height * (blur_diameter / 2.0);
		int side_samples = floor(blur_radius_in_pixels); // half number of full samples, e.g. for a blur diameter 5.2 pixels side_samples would be 2.

		float total_weights = 1.f; // the weight of a central sample
		float sample_weight;

		// sampling left and right side_samples
		for(int i = 1; i <= side_samples; i++){
			sample_weight = (side_samples - i) / blur_radius_in_pixels;
			total_weights += sample_weight * 2;
			sum += read_imagef(image_in, sampler, sample_coord + (float2)(0 , i)) * sample_weight;
			sum += read_imagef(image_in, sampler, sample_coord - (float2)(0 , i)) * sample_weight;
		}

    	sum /= total_weights;
    	write_imagef(image_out, (int2)(x, y), sum);
	
	}
	write_imagef(image_out, (int2)(x, y), sum);
}