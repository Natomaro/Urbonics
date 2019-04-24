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