############################################################
## This file is generated automatically by Vivado HLS.
## Please DO NOT edit it.
## Copyright (C) 2013 Xilinx Inc. All rights reserved.
############################################################
open_project ATAN
set_top fast_atan
add_files atan.cpp
add_files atan.h
add_files -tb atan_imag.txt
add_files -tb atan_out.txt
add_files -tb atan_real.txt
add_files -tb atan_test.cpp
open_solution "solution1"
set_part {xc7z020clg484-1}
create_clock -period 10 -name default
source "./directives.tcl"
