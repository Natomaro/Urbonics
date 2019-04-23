from DROP_scott_thingspeak import doit
from WEP_scott_thingspeak import error_doit

#This needs to be added to serial reading script. 

#the goal of this script is to read the message type and pass it to a 
#function to parse it and send it up to the ThingSpeak channel.


#psudo code
#Read int(hex_input1[2:4]) and call a particular parse function depending on the message type.

#these readings come from the serial readings which still need to be added. 
#example DRoP
hi = "0x1005010000401A000000000000150B13050A0F"
print(hi)
print(type(hi))
reading_from_serial_line = hi

#example WeP
#reading_from_serial_line = hex(0x30010000FF150B13050A0F)

#if int(hex_input1[2:4])
print(reading_from_serial_line[2:4])
if reading_from_serial_line[2:4] == '10':
	print("Givin' you the DRoP, baby (encoding and sending the data)")

	#somewhere, the DRoP message will have count the index value to ensure that all packets have been sent
	doit(reading_from_serial_line)
elif reading_from_serial_line[2:4] == '30':
	print("Don't let that issue be S-WeP-t under the rug, doll (Error message)")
	error_doit(reading_from_serial_line)

