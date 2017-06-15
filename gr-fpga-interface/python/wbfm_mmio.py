import sys
#print(sys.path)
#sys.path.insert(0,'/home/xilinx/pynq')
#sys.path.insert(0,'/home/xilinx/pynq/drivers')

from dma import DMA
from mmio import MMIO
#from pl import Overlay
from numpy import array

class wbfm:
	mmio = MMIO(0x43C10000, 0x00010000)
	array_length = 0

	def __init__(self):
		self.mmio.write(0, 0)

	def accel_start(self):
		data = self.mmio.read(0)
		data = (data & 0x80) | 0x01
		self.mmio.write(0, data)
		#print("Started!")

	def accel_isdone(self):
		data = self.mmio.read(0)
		data = data >> 1
		return ((data & 0x1) > 0)

	def accel_isidle(self):
		data = self.mmio.read(0)
		data = data >> 2
		return ((data & 0x1) > 0)

	def accel_isready(self):
		data = self.mmio.read(0)
		data = ~(data & 0x1)
		return (data > 0)

	def print_status(self):
		data = self.mmio.read(0)
		print("Accelator ka status aa raha hai: " + format(data, '0b'))
	
	def accel_stop(self):
		data = self.mmio.write(0, 0)	
		print("Band kar diya")


'''
ol = Overlay("wbfm_try_1.bit")
ol.download()

# dma_read reads from DDR and sends to Stream
dma_read_addr = int(ol.ip_dict["SEG_axi_dma_from_ps_to_pl_Reg"][0],0)
dma_read = DMA(dma_read_addr, 0)  # 'DMA_TO_DEV'

dma_write_addr = int(ol.ip_dict["SEG_axi_dma_from_pl_to_ps_Reg"][0],0)
dma_write = DMA(dma_write_addr, 1) # 'DMA_FROM_DEV'
x = 0

# ## Debug DMA
# 
# Create some debug functions to print control and status info from DMAs

# In[56]:

dma_read_s = MMIO(dma_read_addr, 128)
dma_write_s = MMIO(dma_write_addr, 128)
# 
# ## Create the DMA buffer 

# In[58]:

def print_dma_status():
    
    print("Read from Memory, Write to FIFO")

    print("MM 2 Stream        Ctrl   : " + format(dma_read_s.read(0x0), '02x'))
    print("Binary                    : " + format(dma_read_s.read(0x0), '0b'))
    print("MM 2 Stream        Status : " + format(dma_read_s.read(0x4), '02x'))
    print("Binary                    : " + format(dma_read_s.read(0x4), '0b'))
    
    print("\nRead from FPGA, Write to Memory")
    
    print("Stream to MM       Ctrl   : " + format(dma_write_s.read(0x30), '02x'))
    print("Binary                    : " + format(dma_write_s.read(0x30), '0b'))
    print("Stream to MM       Status : " + format(dma_write_s.read(0x34), '02x'))
    print("Binary                    : " + format(dma_write_s.read(0x34), '0b'))

def dma_reset_irq():
    control = dma_read_s.read(0x4)
    control = control | 0x1000
    dma_read_s.write(0x4, control)
    
    control = dma_write_s.read(0x34)
    control = control | 0x1000
    dma_write_s.write(0x34, control)

def wait_for_read_transfer():
	data = dma_read_s.read(0x4)
	while(((data & 0x03) != 2)):
		data = dma_read_s.read(0x4)
		#print(~((data & 0x03) == 2))
		#print("Waiting for read transfer")
		#print("MM 2 Stream        Status : " + format(dma_read_s.read(0x4), '02x'))

def wait_for_write_transfer():
	while(((dma_write_s.read(0x34) & 0x03) != 0x02)):
		#print(format(dma_write_s.read(0x34), '02x'))
		#print("Waiting for write transfer")
		pass
j = 0
var = 1500
x = 1
doWork = 2000
dma_read.create_buf(8192)
dma_write.create_buf(8192)
read_buffer = dma_read.get_buf(32)
write_buffer = dma_write.get_buf(32)
#print(write_buffer)
transfer_size_r = 1024
transfer_size_w = 128
count = 0
iter1 = 1024
arr = []
arr2 = [None]*128
arr3 = [None]*128
f = open('WBFM_in.txt', 'r')
f2 = open('WBFM_out.bin', 'ab+')
for line in f:
	if (count == 1536000):
		break
	arr.append(float(line.strip('\n')))
	count = count + 1

acc = mul()
for j in range(var):
	for i in range(transfer_size_w):
		write_buffer[i] = 100;

	for i in range(transfer_size_r):
		read_buffer[i] = arr[i + 1024*j]
	#for i in range(transfer_size_r):
		#print(read_buffer[i])



	#acc.print_status()
	#print(acc.accel_isidle())
	#print(acc.accel_isdone())
	#print(acc.accel_isready())
	acc.accel_start()
	#acc.print_status()

	dma_read.transfer(transfer_size_r*4, 0)
	#print_dma_status()
	#dma_read.transfer(transfer_size*4, 0)
	#print_dma_status()
	wait_for_read_transfer()
	#print("----------------------------")
	#time.sleep(1)
	dma_write.transfer(transfer_size_w*4, 1)
	wait_for_write_transfer()
	#print_dma_status()
	#acc.print_status()

	for i in range(transfer_size_w):
		arr2[i] = write_buffer[i]
		#print(write_buffer[i])
	
	arr3 = array(arr2, 'float32')
	f2.write(arr3)
	print(j)
	#print("----------------------------")

#print(acc.accel_isidle())
#print(acc.accel_isdone())
#print(acc.accel_isready())
f.close()
f2.close()
'''
