import socket               # Import socket module

inputString = input("Enter the input string: ")
s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 9500                # Reserve a port for your service.

s.connect((host, port))

# When client sends "Hello" message, the server send back "Hi"
# When client sends "Test" message which is not "Hello", the server should send back "Goodbye"

byt=inputString.encode()
s.send(byt)
print(s.recv(1024).decode())


s.close()                     # Close the socket when done
