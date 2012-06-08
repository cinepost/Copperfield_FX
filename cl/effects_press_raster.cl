__constant sampler_t sampler = CLK_NORMALIZED_COORDS_TRUE | CLK_ADDRESS_CLAMP_TO_EDGE | CLK_FILTER_LINEAR;

float lerp(float a, float x, float y){
	return a * x + (1.0f - a) * y;
}

__kernel void raster(
        __read_only image2d_t image_in,
        __write_only image2d_t image_out,
        int img_width, int img_height, float density, float dot_size)
      {
	float smooth_bias = 0.1;
    int x = get_global_id(0);
	int y = get_global_id(1);
	float iar = (float)img_width / (float)img_height;
	
	float2 coord = (float2)((float)x / (float)img_width, (float)y / (float)img_height);
    
    float4 in = read_imagef(image_in, sampler, coord);
    in.x = clamp(in.x, 0.1f, 0.9f);
    in.y = clamp(in.y, 0.1f, 0.9f);
    in.z = clamp(in.z, 0.1f, 0.9f);
    
    float kc = 1 - in.x;
    float km = 1 - in.y;
    float ky = 1 - in.z;
    float kk = min(min(kc, km), ky);
    
    float cyan = (kc - kk) / (1 - kk);
	float magenta = (km - kk) / (1 - kk);
	float yellow = (ky - kk) / (1 - kk);
	float black = kk;
    
    // black
    float xx = coord.x*iar*cos(1.178f) - coord.y*sin(1.178f);
	float yy = coord.x*iar*sin(1.178f) + coord.y*cos(1.178f);
	float u = xx * density;
	float v = yy * density;
    
    float su = 1.0f - (u - floor(u)) * 2.0f;
	float sv = 1.0f - (v - floor(v)) * 2.0f;
    
    float val = sqrt(black) * 1.41;
    float d_b = pow(clamp(val - sqrt(su*su + sv*sv), 0.0f, 1.0f), 0.2f);

    // magenta
    xx = (coord.x*iar + 0.5f)*cos(0.392f) - coord.y*sin(0.392f);
	yy = (coord.x*iar + 0.5f)*sin(0.392f) + coord.y*cos(0.392f);
	u = xx * density;
	v = yy * density;
    
    su = 1.0f - (u - floor(u)) * 2.0f;
	sv = 1.0f - (v - floor(v)) * 2.0f;
    
    val = sqrt(magenta)  * 1.41;
    float d_m = pow(clamp(val - sqrt(su*su + sv*sv), 0.0f, 1.0f), 0.2f);

    // cyan
    xx = coord.x*iar*cos(0.785f) - (coord.y + 0.5)*sin(0.785f);
	yy = coord.x*iar*sin(0.785f) + (coord.y + 0.5)*cos(0.785f);
	u = xx * density;
	v = yy * density;
    
    su = 1.0f - (u - floor(u)) * 2.0f;
	sv = 1.0f - (v - floor(v)) * 2.0f;
    
    val = sqrt(cyan)  * 1.41;
    float d_c = pow(clamp(val - sqrt(su*su + sv*sv), 0.0f, 1.0f), 0.2f);

	// yellow
    xx = (coord.x*iar + 0.5f)*cos(1.57f) - (coord.y + 0.5)*sin(1.57f);
	yy = (coord.x*iar + 0.5f)*sin(1.57f) + (coord.y + 0.5)*cos(1.57f);
	u = xx * density;
	v = yy * density;
    
    su = 1.0f - (u - floor(u)) * 2.0f;
	sv = 1.0f - (v - floor(v)) * 2.0f;
    
    val = sqrt(yellow)  * 1.41;
    float d_y = pow(clamp(val - sqrt(su*su + sv*sv), 0.0f, 1.0f), 0.2f);

    
    float3 res = 1;
    
    res *= (float3)(0.05, 0.05, 0.05) * d_b + (float3)(1, 1, 1) * (1 - d_b);
	res *= (float3)(1, 0.05, 1) * d_m + (float3)(1, 1, 1) * (1 - d_m);
	res *= (float3)(1, 1, 0.05) * d_y + (float3)(1, 1, 1) * (1 - d_y);
	res *= (float3)(0.05, 1, 1) * d_c + (float3)(1, 1, 1) * (1 - d_c);

	float4 out = 1;
	out.x = res.x;
	out.y = res.y;
	out.z = res.z;

    write_imagef(image_out, (int2)(x, y), out * 255);
}
