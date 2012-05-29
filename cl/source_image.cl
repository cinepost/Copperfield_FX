const sampler_t smp = CLK_NORMALIZED_COORDS_FALSE | //Natural coordinates
                      CLK_ADDRESS_CLAMP | //Clamp to zeros
                      CLK_FILTER_NEAREST; //Don't interpolate

__kernel void run(__read_only image2d_t img_in, __write_only image2d_t img_out, const int in_width, const int in_height, const int_out_width, const int out_height)
{
	int2 coord = (int2)(get_global_id(0), get_global_id(1));
	float4 val = read_imagef(img_in, smp, coord);	
	val.x = 0;
	//write_imagef(img_out, coord, val);
}

/*
http://www.cmsoft.com.br/index.php?option=com_content&view=category&layout=blog&id=116&Itemid=171
*/

/*
LinkSCEMM_pyOpenCL.pdf
*/
