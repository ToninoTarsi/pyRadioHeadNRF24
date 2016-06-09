#!/usr/bin/python

from cffi import FFI
import time

ffi = FFI()

ffi.cdef("int init();\
	  int setChannel(int c);\
	  int setRF(int dr, int tp);\
	  int send(uint8_t* data, uint8_t len);\
	  int waitPacketSent();\
	  int waitAvailableTimeout(int ms);\
	  int available();\
	  int recv(char* buf, uint8_t* len);\
	  int maxMessageLength();\
	  int isSending();\
	  int printRegisters();\
	  int setNetworkAddress(uint8_t* address, uint8_t len);\
	  int enterSleepMode();\
	  \
	  int managerInit(int address);")

radiohead = ffi.dlopen("./libradiohead.so")

radiohead.init();
radiohead.setChannel(1);
radiohead.setRF(1, 0);

print "StartUp Done!"

print "Receiving..."
buf = ffi.new("char*")
l = ffi.new("uint8_t *")
l[0] = 0

while True:
	if (radiohead.available()):
		b = radiohead.recv(buf, l)
		buf_str = ffi.string(buf)
		print buf_str + " " + str(l[0]) + " " + str(b) 
		
		msg = "AjStyles\0"
		b = radiohead.send(msg, len(msg))
		b = radiohead.waitPacketSent()
		
		time.sleep(1)

#for i in range(0, 10):
#	msg = "AjStyles\0"
#	b = radiohead.send(msg, len(msg))
#	print "Send " + str(b)
#	b = radiohead.waitPacketSent()
#	print "WaitPacketSent " + str(b)
#	time.sleep(1)
