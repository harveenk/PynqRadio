# PynqRadio

This PynqRadio repository contains the following files/folders:

1. WBFM_in.dat: This is the binary raw data file, used as a file source in the GNURadio flow graph.

2. WBFM_pynq_project: This folder contains 2 sub-folders: HLS and Demo. HLS folder has skeleton code for each of the sub-blocks of WBFM. For all the sub-blocks, write your code in the space provided in the design files and test your code with the testbench. Demo folder contains wbfm.cpp file for putting together all 4 sub-blocks and a top level file wrapped_wbfm.cpp.

3. gr-fpga-interface: This folder contains 2 sub-folders: grc and python. All the necessary Python scripts required for building your own custom block can be found in the python folder. grc folder contains the XML file for the block.
