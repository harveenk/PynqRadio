#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright 1970 <+YOU OR YOUR COMPANY+>.
# 
# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
# 
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this software; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
# 

import numpy
import sys
#sys.path.insert(0, '/usr/local/lib/python3.4/dist-packages/pynq')
#print(sys.path)
from gnuradio import gr
from wbfm_mmio import wbfm
from dma import DMA
from mmio import MMIO
#from pl import Overlay
from numpy import array

class dma_try_1(gr.sync_block):
    """
    docstring for block dma_try_1
    """
    def __init__(self, dma_read_addr, mycount, wbfm_base_addr):
        gr.sync_block.__init__(self,
            name="dma_try_1",
            in_sig=[(numpy.float32)],
            out_sig=None)
	
	# dma_read reads from DDR and sends to Stream
	#dma_read_addr = int(dma_read_addr, 0)
        self.dma_read = DMA(dma_read_addr, 0)  # 'DMA_TO_DEV
	
        self.dma_read_s = MMIO(dma_read_addr, 128)
	
        self.dma_read.create_buf(8192)
        self.read_buffer = self.dma_read.get_buf(32)
        self.transfer_size_r = mycount
        self.wbfm = wbfm()
        self.mycount = mycount


    def work(self, input_items, output_items):
        in0 = input_items[0]
        # <+signal processing here+>
	read_buffer = [None]*self.transfer_size_r

        print("input ki length ")
        print(len(in0))
        print(self.transfer_size_r)
        for i in range(0,self.transfer_size_r-1):
                read_buffer[i] = in0[i]
                print(in0[i])
	print("buffer fill ho gaya")
        self.wbfm.accel_start()
        print("accel start ho gaya")
        self.dma_read.transfer(self.transfer_size_r*4, 0)
        self.wait_for_read_transfer()
        print("transfer hp gaya")

        return self.mycount


    def wait_for_read_transfer(self):
        data = self.dma_read_s.read(0x4)
        while(((data & 0x03) != 2)):
               data = self.dma_read_s.read(0x4)
