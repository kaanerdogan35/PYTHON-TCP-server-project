import socket
import time
import json

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
server.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)


content_name = input("Enter Your Username: ")
broadcastJSON = {"ip_address":'localhost',"chunks":[content_name+"_1",content_name+"_2",content_name+"_3",content_name+"_4",content_name+"_5"]}
broadcastJSON = json.dumps(broadcastJSON)
while True:
    server.sendto(broadcastJSON.encode('utf-8'), ('localhost', 5001))
    print("    Announced!  ")
    print(broadcastJSON)
    time.sleep(60)
