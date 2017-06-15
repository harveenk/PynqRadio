############################################################
## This file is generated automatically by Vivado HLS.
## Please DO NOT edit it.
## Copyright (C) 2013 Xilinx Inc. All rights reserved.
############################################################
open_project IIR
set_top iir
add_files iir.cpp
add_files iir.h
add_files -tb iir_in.dat
add_files -tb iir_out.dat
add_files -tb iir_test.cpp
open_solution "solution1"
set_part {xc7z020clg484-1}
create_clock -period 10 -name default
source "./directives.tcl"