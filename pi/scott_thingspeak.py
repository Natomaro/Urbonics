import http.client, urllib.request, urllib.parse, urllib.error
from time import localtime, strftime
import json
import time
import csv
import struct

sleep = 20
#set this key based on our ThingSpeak channel settings. Do not change it unless the channel is modified.
key = 'D0B0N8BK7FHWEP6B'



# Field 1: 'PlanterAddress'
# Field 2: 'Temperature'
# Field 3: 'EC'
# Field 4: 'WaterLevel'
# Field 5: 'Light Validity'
# Field 6: 'Light Count' ## How long it has been on
# Field 7: {RESERVED}
# Field 8: {RESERVED}


## the hex_input in the line below can be used to simulate a DRoP sequence.
##hex_input1 = hex(0x0105010000401A000000000000150B13050A0F)


# just a reminder - a hex digit is four bits, so two digits make a byte


#doit will take a DRoP input and convert the hex value to real values and encode
#them into an HTTP message to be sent to the ThingSpeak channel. 
#To use it, call this function and make the input is a hex(0x00..) value (see hex_input1 example above)

## REMEMBER!! - doit() is for a DRoP message - not a WeP (error message)
def doit(hex_input1):
    
    #Declare the Message, Tag, and Date (month) dictionaries
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
    #cpu_percent = psutil.cpu_percent(interval=1)
    #mem = psutil.virtual_memory()

    messID = Message_Dictionary[int(hex_input1[2:4])] # knowing 0x is hex digits 0-1, messID comes from hex digits 2-3 (byte 1)
    #add here - a small dictionary that maps the message value to the message type string for message ID

    Index = int(hex_input1[4:6],16) #Index is h.d. (hex digits) 4-5 (byte 2), value is a decimal no.
    Planter_address = int(hex_input1[6:8],16) #Address is h.d. 6-7 (byte 3), value is dec. no.
     #Address is h.d. 8-1 (bytes 4 and 5), ADD A DICTIONARY

    Tag = Tag_Dictionary[int(hex_input1[8:12])]

    #Value = str.decode('d',hex_input1[11:27])
    #Value = hex_input1[11:27]
    hexString=str(hex_input1[12:28])#'4002c3c9eecbfb16'
    #print(hexString)
    Value = struct.unpack('<d', struct.pack('Q',int('0x'+hexString, 16)))[0]
    #Value = struct.unpack('d',"3fd5")

    #If we want the date as a colon seperated string
    #Date = str(int(hex_input1[27:29],16)) + ":" + str(int(hex_input1[29:31],16)) + ":" + str(int(hex_input1[31:33],16)) + ":" + str(int(hex_input1[33:35],16)) + ":" + str(int(hex_input1[35:37],16)) + ":" + str(int(hex_input1[37:],16))
    Date = str(format(int(hex_input1[28:30],16),'02')) + ' ' + Date_Dictionary[int(hex_input1[30:32],16)] + " 20"+str(int(hex_input1[32:34],16))
    Timestamp = str(format(int(hex_input1[34:36],16),'02')) + ":" + str(int(hex_input1[36:38],16)) + ":" + str(int(hex_input1[38:],16))

    #This is a breakdown of our example and the expected results
    #0105010000401A000000000000030B13050A0F
    #01 = messID = DRoP
    #05 = Index = Expect 5 more packets after this one
    #01 = Planter Address = planter 1
    #0000 = Tag = pH
    #401A000000000000 = Value (need to cast this to double) = 6.5
    #030B13050A0F = Time = 03 Nov 2019 05:10:15

    #prints for troubleshooting
    print(hex_input1)
    print(messID)
    print(Index)
    print(Planter_address)
    print(Tag)
    print(Value)
    print(Date)
    print(Timestamp)

    #This stuff is a little uncertain for me - Scott made this from ThingSpeak tutorials
    #The gist of it is the params encodes values to field no's and these get sent to the channel.

    params = urllib.parse.urlencode(
            {
            'field1': messID,
            'field2': Index,
            'field3': Planter_address,
            'field4': Tag,
            'field5': Value,
            'field6': Date,
            'field7': Timestamp,
            'key':key
            }
        )
    print(params)

    #params = urllib.urlencode({'field1': temp, 'key':key })
    headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
    conn = http.client.HTTPConnection("api.thingspeak.com:80")
    time.sleep(16)
    try:
        conn.request("POST", "/update", params, headers)#params, headers)
        response = conn.getresponse()

        #print strftime("%a, %d %b %Y %H:%M:%S", localtime())
        print (response.status, response.reason)
        data = response.read()
        conn.close()
    except:
        print ("connection failed")

#for this script, this code runs the doit() function. When necessary though you can call this function passing the hex value the same way.

if __name__ == "__main__":
    while True:
        doit(hex(0x1005010000401A000000000000150B13050A0F))