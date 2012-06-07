__kernel void run(__read_only image2d_t img_in, __write_only image2d_t img_out, sampler_t sampler, int in_width, int in_height, int out_width, int out_height)
{
int x = get_global_id(0);
int y = get_global_id(1);

float2 coord = (float2)((float)x / (float)out_width, (float)y / (float)out_height);


if(x < out_width){
if(y < out_height){
float4 val = read_imagef(img_in, sampler, coord);
write_imagef(img_out, (int2)(x, y), val);
}
}
}

/*
http://www.cmsoft.com.br/index.php?option=com_content&view=category&layout=blog&id=116&Itemid=171
*/

/*
LinkSCEMM_pyOpenCL.pdf
*/


