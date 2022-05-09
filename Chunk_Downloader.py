import socket
import json
import datetime

while True:
    try:
        with open('dictionary.json') as f:
            dicti = json.load(f)

    except:
        print("cdnt open dictionary")
    print(json.dumps(dicti, indent=0, sort_keys=True))
    select=input("Enter the name of chunks to download")

    i=1
    while i<=5:
        try:
            chunkname=select+"_"+str(i)
            print(chunkname)
            TCP_IP=dicti["ip_address"]
            TCP_PORT=8000
            if TCP_IP != -1:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((TCP_IP, TCP_PORT))
                broadcastJSON = {"requested_content": chunkname}
                broadcastJSON = json.dumps(broadcastJSON)
                s.send(broadcastJSON.encode('utf-8'))
                with open("download/"+chunkname,"wb+")as f:
                    while True:
                        data=s.recv(1024)
                        if not data:
                            break
                        f.write(data)
                    f.close()
                    s.close()
                log = open("download/download.txt", 'a')
                an = datetime.datetime.now()
                date = datetime.datetime.strftime(an, '%c')
                senderinfo = '25.53.242.52' + '  /' + chunkname + '  /' + date
                print(senderinfo + '\n' + "Process finish with " + chunkname)
                log.write(senderinfo + "\n")
                log.close()
            i=i+1

        except:
            print(chunkname+" couldn't download")
    content_name = select
    contentloca="download/"+content_name+".png"
    chunknames = [content_name + '_1', content_name + '_2', content_name + '_3', content_name + '_4', content_name + '_5']
    with open(contentloca, 'wb') as outfile:
        for chunk in chunknames:
            with open("download/"+chunk, 'rb') as infile:
                outfile.write(infile.read())
            infile.close()