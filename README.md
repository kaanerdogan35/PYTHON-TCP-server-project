# PYTHON-TCP-server-project
Goal:The goal is to apply the concepts learned in class, through programming and hands-onpractice.  
At the end of this project, you will have a better understanding of how a networkedapplication operates and what are the technologies behind it.
Task:Design and implement a peer-to-peer file sharing application.  The shared design doc-ument specifies the necessary protocols that you need to implement.  Please follow the designdoc closely (in fact, verbatim) in your implementation.
Requirements:The application should;
1.  Have 4 processes: ChunkAnnouncer, ChunkDiscovery, ChunkDownloader, ChunkUploader.These processes should work as outlined in their respective specifications.
2.  Successfully detect the available content in the peers in the Local Area Network.
3.  Successfully download a content from other peers in the Local Area Network.
4.  Display an error dialog if a download is in error.
5.  Output a download/upload log,  containing timestamps,  names and chunk index of alldownloaded files
Please name all your files as [XXX][filename] where XXX is your team members’ initials.You may work in groups of size2 or 3.  You should determine a partitioning of responsi-bilities so that group members can work effectively in parallel.






In our project you have to run chunk_announcer and chunk_discovery firstly.
Chunk_announcer(client) connect the chunk discovery server and ping every 60 seconds. 
Chunk_Discovery save the announcer in contentnamejson JSON file.
Chunk_Discovery and Chunk_Announcer UDP type. and port is 8000.
Second attemp run Chunk_Downloader. 
Chunk_Downloader is a TCP server and use port:5000.
Chunk_Downloader wait connections from any client(Chunk_Uploader).
Third attemp is run the Chunk_Uploader.
When any Client which is Chunk_Uploader is send to data Chunk_Downloader recevied to data.
We use 'UTF-8' format to send and recevied for byte.
Chunk_Uploader take user info and file info from user.
Chunk_Uploader first send filesize data(encode to 'utf-8').
Endly Chunk_uploader send file.
Then send username data(encode to 'utf-8').
Chunk_Downloader recevied functions, take and decode the data. 
Then create chunk_file which has the "'username'.png" .
When process finish, Chunk_Downloader note the user info, file info, date info on 'log.txt'.

