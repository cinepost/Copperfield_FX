__kernel void run(__global const float *a, __global const float *b, __global float *c)
{
	int gid = get_global_id(0);
	float result = a[gid] + b[gid];
	
	// clamping code here
	if(result > 255)result = 255;
	
	c[gid] = result;
}
