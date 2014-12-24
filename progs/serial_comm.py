#!/usr/bin/env python

import json
import serial
import sys
import glob
import time

def serial_ports():
	if sys.platform.startswith('win'):
        	ports = ['COM' + str(i + 1) for i in range(256)]
        	print "windows detected"

 	elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
		# this is to exclude your current terminal "/dev/tty"
		#ports = glob.glob('/dev/tty[A-Za-z]*')
		ports = glob.glob('/dev/ttyU[B-Za-z]*')
		print "linux system"
		print ports
		print type(ports)
		if not ports:
			print "No ports available"
			return "NO_PORT"

	elif sys.platform.startswith('darwin'):
		ports = glob.glob('/dev/tty.*')
		print "darwanian"

	else:
 		raise EnvironmentError('Unsupported platform')
		print "Alien Alien!!"


	result = []
	for port in ports:
 		try:
			if port=="/dev/ttyAMA0":
				pass
			else:
            			print port
				s=serial.Serial(port)
				s.close()
            			result.append(port)
        	except (OSError,serial.SerialException):
            		pass
 	return result


def connect_serial(x):
    print "value of x is %s" %x,type(x)
    x='.'.join(x)
    try:
        ser=serial.Serial(x,9600)
        data=ser.readline()
        print data
        print "Port opened successfully"
    except (OSError,serial.SerialException):
        print "could not open serial port"
    return ser


def parse_serialdata(ser):
        print "in parse serialdata"
	try:
		data=ser.readline()
        	print data
            	buf=json.loads(data)
	except:
		print "json error : could not load"
	try:
                vfile=open('vdata.txt','a+')
                cfile=open('cdata.txt','a+')
                vfile.write(str(buf['Voltage']))
                vfile.write('\n')
                cfile.write(str(buf['Current']))
                cfile.write('\n')
                vfile.close()
                cfile.close()
	except IOError as e:
                print "can't open file",e.strerror

def grab_serial(ser):
	print "in serial grabber"
	try:
		data=ser.readline()
		print data
	except:
		print "read line failed"
	try:
		myfile=open("serial_capture.txt","a+")
		myfile.write(data)
		myfile.write('\n')
		myfile.close()
	except:
		print "can't open file"

def main():
	print "in main"
	x=serial_ports()
	while True:
		if x!="NO_PORT":
			serial_obj=connect_serial(x)
			time.sleep(1)
			#parse_serialdata(serial_obj)
		else :
			print "no port available, try after some time"
			time.sleep(10)
			x=serial_ports()
		

if __name__=="__main__":
    main()
