############################################################
## This file is generated automatically by Vivado HLS.
## Please DO NOT edit it.
## Copyright (C) 2013 Xilinx Inc. All rights reserved.
############################################################
open_project VOLK
set_top volk
add_files volk.cpp
add_files volk.h
add_files -tb volk_in_i.txt
add_files -tb volk_in_r.txt
add_files -tb volk_out_i.txt
add_files -tb volk_out_r.txt
add_files -tb volk_test.cpp
open_solution "solution1"
set_part {xc7z020clg484-1}
create_clock -period 10 -name default
source "./directives.tcl"
