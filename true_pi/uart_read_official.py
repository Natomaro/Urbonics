#!/usr/bin/env python
import time
import serial
import csv

ser = serial.Serial(
        port=' /dev/ttyUSB0',
        baudrate = 9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
)

while 1:
        x=ser.readline()
        print (x)
        bit_input=str(x)

        # first_data_in_binary = bit_input[0:2].encode()
        # first_data_in_decimal = int(first_data_in_binary,2)
        # print (first_data_in_binary, first_data_in_decimal)

        # last_data_in_binary = bit_input[4:8].encode()
        # last_data_in_decimal = int(last_data_in_binary,2)
        # print (last_data_in_binary, last_data_in_decimal)

        with open('controller_data.csv', mode = 'a') as data:
            data_writer = csv.writer(data,delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL,skipinitialspace = False,lineterminator = '\n',)
            data_writer.writerow([bit_input])