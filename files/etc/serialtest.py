#!/usr/bin/env python
import serial
import io
import sys

#https://pyserial.readthedocs.org/en/latest/index.html

try:
	print("Checking if GPIO 14 & 15 are connected")
	#ser = serial.serial_for_url('loop://', timeout=1) #Tester
	
	#Standard UART on RPi: need to use raspi-config to disable bootup logging on SERIAL 
	ser = serial.serial_for_url('/dev/ttyAMA0', timeout=1) 
	ser.write("hello\n")
	ser.flush() # it is buffering. required to get the data out *now*
	hello = ser.readline()
	if(hello == "hello\n"):
		print("GPIO 14 & 15 are connected")
		sys.exit(0)
	else:
		print("Expected Message Not Received")
		sys.exit(1)
except serial.SerialException:
	print("Serial Communication Failed")
	sys.exit(1)

