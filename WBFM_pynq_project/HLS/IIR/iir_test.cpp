#include "iir.h"
#include <math.h>
#include <stdio.h>
#include <stdlib.h>



int main()
{
	float output[1001] = {0, };
	float input[1000] = {0, };
	float golden_out;

	FILE *fp_in, *fp_out;

	fp_in=fopen("iir_in.dat", "r");
	if(fp_in==NULL)
	{
		printf("cannot open iir_in.dat\n");
		return -1;
	}

	fp_out=fopen("iir_out.dat", "r");
	if(fp_out==NULL)
	{
		printf("cannot open iir_out.dat\n");
		return -1;
	}

	int j, fail;
	fail = 0;

	for(j= 0; j<1001; j++){
		fscanf(fp_in, "%f", &input[j]);
	}

	for (j = 0; j < 995; j++)
	{
		iir(input[j], &output[j], 1);
	}

	for(j = 0; j<995; j++){
		fscanf(fp_out, "%f", &golden_out);
		if(fabs(output[j] - golden_out) > 0.00001)
		{
			printf("j=%d: out=%f, golden=%f\n", j, output[j], golden_out);
			fail = 1;
		}
	}

	fclose(fp_in);
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
