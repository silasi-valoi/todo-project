import socket

host = ''
port = 8080



c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
c.bind((host, port))
c.listen(1)

print('Web server is running on port 8080...')
	
while True:    
    # Wait for client connections
    client_connection, client_address = c.accept()

    # Get the client request
    request = client_connection.recv(1024).decode()
    #print(request)
	
    # Parse HTTP headers
    headers = request.split('\n')
    filename = headers[0].split()[1]
    print(headers, filename)

    # Send HTTP response
    response = 'HTTP/1.0 200 OK\n\nHello World'
    client_connection.sendall(response.encode())
    client_connection.close()

# Close socket
server_socket.close()
  


