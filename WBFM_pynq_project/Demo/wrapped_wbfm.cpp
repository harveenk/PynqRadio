#include <assert.h>
#include <ap_axi_sdata.h>
#include "wbfm.h"

typedef ap_axiu<32,4,5,5> AXI_VAL;
#define ARR_SIZE 8
typedef ap_axiu<32,4,5,5> AXI_VAL;

template <typename T, int U, int TI, int TD>
T pop_stream(ap_axiu <sizeof(T)*8,U,TI,TD> const &e)
{
#pragma HLS INLINE

	assert(sizeof(T) == sizeof(int));
	union
	{
		int ival;
		T oval;
	} converter;
	converter.ival = e.data;
	T ret = converter.oval;

	volatile ap_uint<sizeof(T)> strb = e.strb;
	volatile ap_uint<sizeof(T)> keep = e.keep;
	volatile ap_uint<U> user = e.user;
	volatile ap_uint<1> last = e.last;
	volatile ap_uint<TI> id = e.id;
	volatile ap_uint<TD> dest = e.dest;

	return ret;
}

template <typename T, int U, int TI, int TD> ap_axiu <sizeof(T)*8,U,TI,TD> push_stream(T const &v, bool last = false)
{
#pragma HLS INLINE
	ap_axiu<sizeof(T)*8,U,TI,TD> e;

	assert(sizeof(T) == sizeof(float));
	union
	{
		int oval;
		T ival;
	} converter;
	converter.ival = v;
	e.data = converter.oval;

	// set it to sizeof(T) ones
	e.strb = -1;
	e.keep = 15; //e.strb;
	e.user = 0;
	e.last = last ? 1 : 0;
	e.id = 0;
	e.dest = 0;
	return e;
}

template <int SIZE, int U, int TI, int TD>
void wrapped_wbfm(AXI_VAL in_stream[SIZE], AXI_VAL out_stream[SIZE/8])
{
  float input[SIZE], output[SIZE/8];

// stream in input of SIZE
for(int i=0; i<SIZE; i++)
{
     #pragma HLS PIPELINE II=1
     input[i] = pop_stream<float,U,TI,TD>(in_stream[i]);
  }

  //  do  multiplication
  WBFM_top(input,output);

//output is SIZE/8
for (int i=0; i<SIZE/8; i++)
   {
     #pragma HLS PIPELINE II=1
       out_stream[i] = push_stream<float,U,TI,TD>(output[i], i== (SIZE/8 -1));
}
}
// this is the top level design that will be synthesized into RTL
void WBFM_accel(AXI_VAL INPUT_STREAM[MYCOUNT], AXI_VAL OUTPUT_STREAM[MYCOUNT/8])
{
   // Map ports to Vivado HLS interfaces
#pragma HLS INTERFACE s_axilite port=return bundle=CONTROL_BUS
#pragma HLS INTERFACE axis port=INPUT_STREAM
   #pragma HLS INTERFACE axis port=OUTPUT_STREAM
   wrapped_wbfm<MYCOUNT,4,5,5>(INPUT_STREAM,   OUTPUT_STREAM);
}


