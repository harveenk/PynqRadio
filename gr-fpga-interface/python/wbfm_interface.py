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
from gnuradio import gr
from wbfm_mmio import wbfm
from dma import DMA
from mmio import MMIO
from numpy import array

class wbfm_interface(gr.decim_block):
    """
    docstring for block wbfm_interface
    """
    def __init__(self, dma_read_addr, dma_write_addr, wbfm_base_addr, mycount):
        gr.decim_block.__init__(self,
            name="wbfm_interface",
            in_sig=[numpy.float32],
            out_sig=[numpy.float32], decim=8)
        
        self.dma_read = DMA(dma_read_addr, 0)  # 'DMA_TO_DEV
        self.dma_read_s = MMIO(dma_read_addr, 128)
        self.dma_read.create_buf(8192)
        self.read_buffer = self.dma_read.get_buf(32)
        self.dma_write = DMA(dma_write_addr, 1)  # 'DEV_TO_DMA
        self.dma_write_s = MMIO(dma_write_addr, 128)
        self.dma_write.create_buf(8192)
        self.write_buffer = self.dma_write.get_buf(32)
        self.transfer_size_r = mycount 
        self.transfer_size_w = mycount/8
        self.wbfm = wbfm()
        self.mycount = mycount



    def work(self, input_items, output_items):
        in0 = input_items[0]
        arr = []
        out = output_items[0]
        
        #print("input length ")
        if (len(in0) > 1024):
            for j in range(len(in0)/1024):
	    #read_buffer = [None]*self.transfer_size_r
	    #write_buffer = [None]*self.transfer_size_w

            #print("input length")
            #print(len(in0))
            #print(self.transfer_size_r)
                for i in range(self.transfer_size_r):
                    self.read_buffer[i] = in0[i + j*1024]
                    #print(in0[i + j*1024])
	    #print("buffer filled up")
            #self.wbfm.print_status()
                self.wbfm.accel_start()
            #self.wbfm.print_status()
            #print("accel started")
                self.dma_read.transfer(self.transfer_size_r*4, 0)
                self.wait_for_read_transfer()
            #print("read transfer done")
            #print("About to start write transfer")
	        self.dma_write.transfer(self.transfer_size_w*4, 1)
	        self.wait_for_write_transfer()
            #print("Write transfer done!!")
            
                for i in range(self.transfer_size_w):
                    arr.append(self.write_buffer[i])
                #print(self.write_buffer[i])
                #print("Size of arr: ")
                #print(len(arr))
 
            out[:] = arr
        
        return len(output_items[0])
     
    
    def wait_for_read_transfer(self):
        data = self.dma_read_s.read(0x4)
        while(((data & 0x03) != 2)):
            data = self.dma_read_s.read(0x4)

    
    def wait_for_write_transfer(self):
        while(((self.dma_write_s.read(0x34) & 0x03) != 0x02)):
            #print(format(self.dma_write_s.read(0x34),'02x'))
            #self.wbfm.print_status()
            #print("waiting")
            pass
