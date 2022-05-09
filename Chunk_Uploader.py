import socket
import json
import os
import math
import datetime
content_name=input("What is your file name? :")
filename = "upload/"+content_name+'.png'
c = os.path.getsize(filename)
CHUNK_SIZE = math.ceil(math.ceil(c)/5)
index = 1
with open(filename, 'rb') as infile:
    chunk = infile.read(int(CHUNK_SIZE))
    while chunk:
        chunkname ="upload/"+ content_name+'_'+str(index)
        with open(chunkname,'wb+') as chunk_file:
            chunk_file.write(chunk)
        index += 1
        chunk = infile.read(int(CHUNK_SIZE))
chunk_file.close()


while True:
    TCP_IP = ''
    TCP_PORT = 8000
    BUFFER_SIZE = 1024

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((TCP_IP, TCP_PORT))
    s.listen(1)
    try:
        conn, addr = s.accept()
        g=conn.recv(1024)
        gelen = g.decode('utf-8')
        geljson = json.loads(gelen)
        chunkname=geljson["requested_content"]
        chunknameloca="upload/"+geljson["requested_content"]
        with open(chunknameloca,"rb")as f:
            data = f.read(1024)
            conn.send(data)
            while data:
                data = f.read(1024)
                conn.send(data)
            conn.close()
            print("a")
            f.close()
        an = datetime.datetime.now()
        date = datetime.datetime.strftime(an, '%c')
        senderinfo = str(addr) + '  /' + chunkname + '  /' + date
        log=open("upload/uploadlog.txt",'a')
        print(senderinfo + '\n' + "Process finish with " + chunkname)
        log.write(senderinfo + "\n")
        log.close()
    except:
        print(chunkname+"couldn't upload")