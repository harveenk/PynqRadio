#ifndef WBFM_H
#define WBFM_H

#include <stdio.h>
#include <math.h>
#include <stdlib.h>

#define MYCOUNT  1024

void volk(float outputVector[MYCOUNT], float inputVector[MYCOUNT]);
void fir(float * result, float input, unsigned short do_filter);
void iir(float input, float *output, int size);
float fast_atan(float y, float x);
void WBFM_top(float in[MYCOUNT], float out[MYCOUNT/8]);

#endif
