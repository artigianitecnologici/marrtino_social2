import socket               # Import socket module

SERVER_ADDRESS = '10.3.1.1'             #           socket.gethostname() # Get local machine name
SERVER_PORT = 9000                 # Reserve a port for your service.
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind((SERVER_ADDRESS, SERVER_PORT))        # Bind to the port
serverSocket.listen(1)

print("Server waiting on (%s, %d)" % (SERVER_ADDRESS, SERVER_PORT))
connectionSocket, clientAddress = serverSocket.accept() 

while True:
   # receive request on newly established connectionSocket
   request = connectionSocket.recv(1024)
   #print("Received request from (%s, %d)" % (clientAddress[0], clientAddress[1]))
   print("Request : (%s)" % (request))
   # convert message to upper case
   response = request.upper()
   # send back modified string to client
   connectionSocket.send(response)
   print("Sent reply to (%s, %d)" % (clientAddress[0], clientAddress[1]))

print("Close connection on %d" % SERVER_PORT)
connectionSocket.close()
