import socket                                         
# Create a socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# Get local machine name
host = socket.gethostname()
print(host)
port = 9999

# Bind to the port
serversocket.bind((host, port))                                  
# Queue up to 5 requests
serversocket.listen(5) 

while True:
   # Establish a connection
   clientsocket,addr = serversocket.accept()      
   print("Got a connection from %s" % str(addr))
   msg = 'Thank you for connecting'+ "\r\n"
   clientsocket.send(msg.encode('ascii'))
   clientsocket.close()
