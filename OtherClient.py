import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 9500                # Reserve a port for your service.

s.connect((host, port))

# When client sends "Test" message which is not "Hello", the server should send back "Goodbye"
st='Test'
byt=st.encode()
s.send(byt)
print(s.recv(1024).decode())

s.close()                     # Close the socket when done
