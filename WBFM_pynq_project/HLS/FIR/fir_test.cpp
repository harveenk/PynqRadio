#include "fir.h"

#include <stdio.h>
#include <math.h>
#include <stdlib.h>

int main()
{
	float  out;
	float  input;
	float  gold;

	FILE *fp_in, *fp_out;
	fp_in=fopen("fir_in.txt", "r");
	if(fp_in==NULL)
	{
		printf("cannot open fir_in.txt\n");
		return -1;
	}

	fp_out=fopen("fir_out.txt", "r");
	if(fp_out==NULL)
	{
		printf("cannot open fir_out.txt\n");
		return -1;
	}

	int j, fail;
	fail = 0;
	gold = 0;

	for(j= 0; j<1000; j++){
		fscanf(fp_in, "%f", &input);
		fir(&out, input, j%4);//audio decimation is 4

		if(!(j%4))
		{
			if(j>307)// first 308 output are not from current input
			{
				fscanf(fp_out, "%f", &gold);
				if(fabs(out-gold) > 0.00001 )
				{
					printf("j=%d: out=%f, golden=%f\n", j, out, gold);
					fail = 1;
				}
			}
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
