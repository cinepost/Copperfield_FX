__constant sampler_t sampler = CLK_NORMALIZED_COORDS_TRUE | CLK_ADDRESS_REPEAT | CLK_FILTER_LINEAR;

inline float level(float in , float min, float max){
	float out = clamp(in - min, 0.0f, 1.0f);
	out *= (1.0f / max);
	return out;
};

__kernel void raster(
        __read_only image2d_t image_in,
        __write_only image2d_t image_out,
        int img_width, int img_height, float density, int quality)
      { 
    float smooth_bias = 0.02f; 
    int x = get_global_id(0);
	int y = get_global_id(1);
	float iar = (float)img_width / (float)img_height;
	
	float3 acc = 0.0f;
	
	for( int a=0; a < quality; a++){
		for( int b=0; b < quality; b++){
			
			float2 coord = (float2)(((float)x + (float)a / (float)quality)/ (float)img_width, ((float)y + (float)b / (float)quality) / (float)img_height);
		    
		    float4 in = read_imagef(image_in, sampler, coord);
		    in.x = level(pow(in.x,0.5f), 0.1f, 0.9f);
		    in.y = level(pow(in.y,0.5f), 0.1f, 0.9f);
		    in.z = level(pow(in.z,0.5f), 0.1f, 0.9f);
		    
		    float kc = 1.0f - in.x;
		    float km = 1.0f - in.y;
		    float ky = 1.0f - in.z;
		    float kk = min(min(kc, km), ky);
		    
		    float cyan = (kc - kk) / (1.0f - kk);
			float magenta = (km - kk) / (1.0f - kk);
			float yellow = (ky - kk) / (1.0f - kk);
			float black = kk;
		    
		    // black
		    float xx = coord.x*iar*cos(1.178f) - coord.y*sin(1.178f);
			float yy = coord.x*iar*sin(1.178f) + coord.y*cos(1.178f);
			float u = xx * density;
			float v = yy * density;
		    
		    float su = 0.7f - (u - floor(u)) * 1.5f;
			float sv = 0.7f - (v - floor(v)) * 1.5f;
		    
		    float val = sqrt(black) / 1.03f;
		    float d_b = smoothstep(clamp(val + smooth_bias, 0.0f, 1.0f), clamp( val - smooth_bias, 0.0f , 1.0f), sqrt(su*su + sv*sv));
		
		    // magenta
		    xx = (coord.x*iar + 0.5f)*cos(0.392f) - coord.y*sin(0.392f);
			yy = (coord.x*iar + 0.5f)*sin(0.392f) + coord.y*cos(0.392f);
			u = xx * density;
			v = yy * density;
		    
		    su = 0.7f - (u - floor(u)) * 1.5f;
			sv = 0.7f - (v - floor(v)) * 1.5f;
		    
		    val = sqrt(magenta) / 1.03f;
		    float d_m = smoothstep(clamp(val + smooth_bias, 0.0f, 1.0f), clamp( val - smooth_bias, 0.0f , 1.0f), sqrt(su*su + sv*sv));
		
		    // cyan
		    xx = coord.x*iar*cos(0.785f) - (coord.y + 0.5f)*sin(0.785f);
			yy = coord.x*iar*sin(0.785f) + (coord.y + 0.5f)*cos(0.785f);
			u = xx * density;
			v = yy * density;
		    
		    su = 0.7f - (u - floor(u)) * 1.5f;
			sv = 0.7f - (v - floor(v)) * 1.5f;
		    
		    val = sqrt(cyan) / 1.03f;
		    float d_c = smoothstep(clamp(val + smooth_bias, 0.0f, 1.0f), clamp( val - smooth_bias, 0.0f , 1.0f), sqrt(su*su + sv*sv));
		
			// yellow
		    xx = (coord.x*iar + 0.5f)*cos(1.57f) - (coord.y + 0.5)*sin(1.57f);
			yy = (coord.x*iar + 0.5f)*sin(1.57f) + (coord.y + 0.5)*cos(1.57f);
			u = xx * density;
			v = yy * density;
		    
		    su = 0.7f - (u - floor(u)) * 1.5f;
			sv = 0.7f - (v - floor(v)) * 1.5f;
		    
		    val = sqrt(yellow) / 1.03f;
		    float d_y = smoothstep(clamp(val + smooth_bias, 0.0f, 1.0f), clamp( val - smooth_bias, 0.0f , 1.0f), sqrt(su*su + sv*sv));
		
		    
		    float3 res = 1.0f;
		    
		    res *= (float3)(0.05f, 0.05f, 0.05f) * d_b + (float3)(1.0f, 1.0f, 1.0f) * (1.0f - d_b);
			res *= (float3)(1.0f, 0.05f, 1.0f) * d_m + (float3)(1.0f, 1.0f, 1.0f) * (1.0f - d_m);
			res *= (float3)(1.0f, 1.0f, 0.05f) * d_y + (float3)(1.0f, 1.0f, 1.0f) * (1.0f - d_y);
			res *= (float3)(0.05f, 1.0f, 1.0f) * d_c + (float3)(1.0f, 1.0f, 1.0f) * (1.0f - d_c);
			acc += res;
		}	
	}

	acc /= quality * quality;

	float4 out = 1.0f;
	out.x = acc.x;
	out.y = acc.y;
	out.z = acc.z;

    write_imagef(image_out, (int2)(x, y), out);
}
