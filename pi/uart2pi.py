#import wiringpi
#wiringpi.wiringPiSetup()
#serial = wiringpi.serialOpen('/dev/ttyAMA0',9600)
#wiringpi.serialPuts(serial,'hello world!')

import csv
import struct
## Simulate a DRoP sequence. There is going to be 6 packets, a full data request.
## 
#
hex_input1 = hex(0x0105010000401A000000000000150B13050A0F)

Message_Dictionary = {
    10:"DRoP",
}

Tag_Dictionary = {
    0:'pH',
    1:'EC',
    2:"Water Level",
    3:"Light Validity",
    4:'Light Count',
    5:'Fluid Motion',
    6:'Env Temp'
}

Date_Dictionary = {
    1:'Jan',
    2:'Feb',
    3:'Mar',
    4:'Apr',
    5:'May',
    6:'Jun',
    7:'Jul',
    8:'Aug',
    9:'Sep',
    10:'Oct',
    11:'Nov',
    12:'Dec',

}

#string = str(hex_input1)
# just a reminder - a hex digit is four bits, so two digits make a byte
messID = Message_Dictionary[int(hex_input1[2:4])] # knowing 0x is hex digits 0-1, messID comes from hex digits 2-3 (byte 1)
#add here - a small dictionary that maps the message value to the message type string for message ID

Index = int(hex_input1[3:5],16) #Index is h.d. (hex digits) 4-5 (byte 2), value is a decimal no.
Planter_address = int(hex_input1[5:7],16) #Address is h.d. 6-7 (byte 3), value is dec. no.
 #Address is h.d. 8-1 (bytes 4 and 5), ADD A DICTIONARY
Tag = Tag_Dictionary[int(hex_input1[7:11],16)]
#Value = str.decode('d',hex_input1[11:27])
#Value = hex_input1[11:27]
hexString=str(hex_input1[11:27])#'4002c3c9eecbfb16'
#print(hexString)
Value = struct.unpack('<d', struct.pack('Q',int('0x'+hexString, 16)))[0]
#Value = struct.unpack('d',"3fd5")

#If we want the date as a colon seperated string
#Date = str(int(hex_input1[27:29],16)) + ":" + str(int(hex_input1[29:31],16)) + ":" + str(int(hex_input1[31:33],16)) + ":" + str(int(hex_input1[33:35],16)) + ":" + str(int(hex_input1[35:37],16)) + ":" + str(int(hex_input1[37:],16))
Date = str(format(int(hex_input1[27:29],16),'02')) + ' ' + Date_Dictionary[int(hex_input1[29:31],16)] + " 20"+str(int(hex_input1[31:33],16))
Timestamp = str(format(int(hex_input1[33:35],16),'02')) + ":" + str(int(hex_input1[35:37],16)) + ":" + str(int(hex_input1[37:],16))

#0105010000401A000000000000030B13050A0F
#01 = messID = DRoP
#05 = Index = Expect 5 more packets after this one
#01 = Planter Address = planter 1
#0000 = Tag = pH
#401A000000000000 = Value (need to cast this to double) = 6.5
#030B13050A0F = Time = 03 Nov 2019 05:10:15

print(hex_input1)
print(messID)
print(Index)
print(Planter_address)
print(Tag)
print(Value)
print(Date)
print(Timestamp)


with open('controller_data.csv', mode = 'a') as data:
    data_writer = csv.writer(data,delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL,skipinitialspace = False,lineterminator = '\n',)
    data_writer.writerow([messID,Index,Planter_address,Tag,Value,Date,Timestamp,hex_input1])
