import socket
import time

# Proxy server address and port
PROXY_HOST = '127.0.0.1'
PROXY_PORT = 8888

# Create a socket for the client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((PROXY_HOST, PROXY_PORT))

def send_set_request(index, data):
    message = f"SET IND={index} DATA={data};"
    client_socket.sendall(bytes(message, 'utf-8'))
    time.sleep(0.5)
    response = client_socket.recv(1024)
    print("Response from proxy server:")
    print(response.decode('utf-8'))

# Function to send a SET request to the proxy server
def send_set():
    # Prompt the user for index and data
    index = input("Enter index: ")
    data = input("Enter data: ")
    # Send the SET request to the proxy server
    send_set_request(index, data)

while True:
    # Prompt the user for the operation
    operation = input("Enter operation (set/get/reset/evict): ")
    if operation == "set":
        send_set()
    else:
        print("Invalid operation. Please enter 'set' to perform a SET operation.")
