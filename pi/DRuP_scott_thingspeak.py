import http.client, urllib.request, urllib.parse, urllib.error
from time import localtime, strftime
import json
import time
import csv
import struct


#doit will take a DRoP input and convert the hex value to real values and encode
#them into an HTTP message to be sent to the ThingSpeak channel. 
#To use it, call this function and make the input is a hex(0x00..) value (see hex_input1 example above)

## REMEMBER!! - doit() is for a DRoP message - not a WeP (error message)
def dum_dum_shit_doit():
    
    #Declare the Message, Tag, and Date (month) dictionaries
    Message_Dictionary = {
        "DRuP":0x01,
    }

    Tag_Dictionary = {
        'pH':0,
        'EC':1,
        "Water Level":2,
        "Light Validity":3,
        'Light Count':4,
        'Fluid Motion':5,
        'Env Temp':6,
    }

 
    #This stuff is a little uncertain for me - Scott made this from ThingSpeak tutorials
    #The gist of it is the params encodes values to field no's and these get sent to the channel.

    data_from_website = urllib.request.urlopen("https://api.thingspeak.com/channels/732724/feeds.json?api_key=Q79JTILGZLQ92YKG&results=2")
    s = str(data_from_website.read())
    data_from_website.close()

    print(type(s))
    j = s.split("\"entry_id\":1,")[1]
    #str_field0 = j.split("field1\":\"")[1]
    str_field1 = j.split("}")[0] #str_field0.split("}")[0]
    print(j)
    new_string = str_field1.replace("\"","")
    new_string_list = new_string.split(',')
    print(new_string_list)

    #new string has a list with all the fields and their data
    #its all in string types because that was the easiest way to cut it up/edit it, etc.
    #new_string has the field<no>: still - needs to be removed before converting to hex

    #messageID
    messID_string = new_string_list[0].replace("field1:","")
    messID_hold = Message_Dictionary[messID_string]
    messID = "0x{:02x}".format(messID_hold)
    print(messID_string)
    print(messID)


    #Planter Address
    PA_string = new_string_list[1].replace("field2:","")
    PA = "0x{:02x}".format(int(PA_string))
    print(PA_string)
    print(PA)

    #Tag
    Data_Request_string = new_string_list[2].replace("field3:","")
    DR_hold = Tag_Dictionary[Data_Request_string]
   # DR = "0x{:0002x}".format(int(DR_hold))
    DR = format(int(DR_hold),'04x')
    print(Data_Request_string)
    print(DR)
    print(type(DR))


    #format(int(hex_input1[34:36],16),'02')

    Message_str = format(int(messID_hold),'02x')+format(int(PA_string),'02x')+format(int(DR_hold),'04x')
    print(Message_str)


    #After a bunch of fun gymnastics, I made the string back into an int type (which using hex() can be read in hex notation)
    #This int data type is what we should expect from the controller (i.e. a number, not a string)
    Message = int(Message_str,16)
    print(hex(Message))
    print(type(Message))


dum_dum_shit_doit()