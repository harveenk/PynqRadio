#include "atan.h"

#include <math.h>
#include <stdio.h>
#include <stdlib.h>

int main()
{
	float d_gain = 0.002122;
	float output_f;
	float input_real;
	float input_imag;
	float golden_output;

	FILE *fp_in_r, *fp_in_i, *fp_out;

	fp_in_i=fopen("atan_real.txt", "r");	/* wrong name!! */
	if(fp_in_r==NULL)
	{
		printf("cannot open atan_real.txt\n");
		return -1;
	}

	fp_in_r=fopen("atan_imag.txt", "r");	/* wrong name!! */
	if(fp_in_i==NULL)
	{
		printf("cannot open atan_imag.txt\n");
		return -1;
	}

	fp_out=fopen("atan_out.txt", "r");
	if(fp_out==NULL)
	{
		printf("cannot open atan_out.txt\n");
		return -1;
	}

	int j, fail;
	fail = 0;

	for(j= 0; j<1000; j++){
		fscanf(fp_in_i, "%f", &input_imag);
		fscanf(fp_in_r, "%f", &input_real);
		output_f = fast_atan(input_real, input_imag);
		output_f = output_f*d_gain;
		fscanf(fp_out, "%f", &golden_output);
		if(fabs(output_f - golden_output) > 0.00001)
		{
			printf("j=%d: x=%.10f, y=%.10f, out_f=%.10f, golden=%.10f\n", j, input_real, input_imag, output_f, golden_output);
			fail = 1;
		}
	}

	fclose(fp_in_r);
	fclose(fp_in_i);
	fclose(fp_out);

	if(fail)
	{
		printf("\n\nFailed!!\n\n");
	}
	else
	{
		printf("\n\nSuccess!!\n\n");
	}

	return 0;
}
