import socket
import json


client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
client.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
client.bind(('localhost', 5001))

data = {}

while True:
    msg, addr = client.recvfrom(1024)
    gelen = msg.decode('utf-8')
    geljson = json.loads(gelen)
    
    try:
        print("Announce received, " +": "+geljson["ip_address"]+": "+geljson["chunks"][0]+","+geljson["chunks"][1]+","+geljson["chunks"][2]+","+geljson["chunks"][3]+geljson["chunks"][4])
    except:
        print("Announce might be in wrong format, received from: " + addr[0])


    with open('dictionary.json', 'w') as f:
        json.dump(geljson,f)





    