import socket
import threading

HOST = '192.168.132.36'
PORT = 1234
LISTENER_LIMIT = 5
active_clients = []

def listen_for_massages(client, username):


def listen_for_messages_from_server(client):
    try:
        while True:
            message = client.recv(BUFFER_SIZE).decode('utf-8')
            if not message:
                print("Message received from the server is empty")
                break

            username, content = message.split("~", 1)
            print(f"[{username}] {content}")
    except (socket.error, ValueError) as e:
        print(f"Error in listen_for_messages_from_server: {e}")

def send_massage_to_client(client, massage):
	client.sendall(massage.encode())

def send_massage_to_all(from_username, massage):
	for user in active_clients:
		send_massage_to_client(client[1], massgae)


def client_handler(client):

	while 1:
		username = client.recv(2048).decode('utf-8')

		if username != '':
			active_clients.append((username, client))
		else:
			print("Client username is empty")

def main():
	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	print(f"Running the server on {HOST} {PORT}")

	try:
		server.bind((HOST, PORT))
	except:
		print(f"Unable to bind to host {HOST} and port {PORT}")

	server.listen(LISTENER_LIMIT)

	while 1:
		client, address = server.accept()
		print("Successfully connected to server {address[0]} {address[1]}")

		threading.Thread(target=client_handler, args=(client, )).start()

	threading.Thread(target=client_handler, args=(client, )).start()

if __name__ == '__main__':
	main()