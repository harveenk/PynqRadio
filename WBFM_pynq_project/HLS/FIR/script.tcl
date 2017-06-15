############################################################
## This file is generated automatically by Vivado HLS.
## Please DO NOT edit it.
## Copyright (C) 2014 Xilinx Inc. All rights reserved.
############################################################
open_project FIR
set_top fir
add_files fir.cpp
add_files fir.h
add_files -tb fir_in.txt
add_files -tb fir_out.txt
add_files -tb fir_test.cpp
open_solution "solution1"
set_part {xc7z020clg484-1}
create_clock -period 10 -name default
source "./directives.tcl"
