#!/usr/bin/env python

import json
import serial
import sys
import glob
import time

def serial_ports():
    if sys.platform.startswith('win'):
        ports = ['COM' + str(i + 1) for i in range(256)]
        #print "windows detected"

    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this is to exclude your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')
        #print "linux system"

    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
        #print "darwanian"

    else:
        raise EnvironmentError('Unsupported platform')
        #print "Alien Alien!!"

    result = []
    for port in ports:
        try:
            #print port
            s=serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError,serial.SerialException):
            pass
    return result


def connect_serial(x):
    #print "value of x is %s" %x,type(x)
    x='.'.join(x)
    try:
        ser=serial.Serial(x,9600)
        data=ser.readline()
        #print data
        print "Port opened successfully"
    except (OSError,serial.SerialException):
        print "could not open serial port"
    return ser


def parse_serialdata(ser):
        #print "in parse serialdata"
        while True:
            data=ser.readline()
            #print data
            buf=json.loads(data)
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

            print buf['Voltage'],buf['Current']
            time.sleep(0.5)


def main():
    #print "in main"
    x=serial_ports()
    serial_obj=connect_serial(x)
    parse_serialdata(serial_obj)



if __name__=="__main__":
    main()
