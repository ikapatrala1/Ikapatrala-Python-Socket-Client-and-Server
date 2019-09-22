import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 9500                # Reserve a port for your service.
s.bind((host, port))        # Bind to the port

s.listen(10)                 # Now wait for client connection.
while True:
   c, addr = s.accept()     # Establish connection with client.
   print('Got connection from', addr)
   inputData=c.recv(2000)
   data = inputData.decode()
   if(data=='Hello'):
       message = 'Hi'
   else:
       message = 'Goodbye'
   c.sendto(message.encode(),(host, port))
   c.close()                # Close the connection