import socket
import threading

HOST = '192.168.132.36'
PORT = 1234
BUFFER_SIZE = 2048

def listen_for_massages_from_server(client):

	while True:
		massage = client.recv(BUFFER_SIZE).decode('utf-8')
		if massage != '':
			username = massage.split("~")[0]
			content = massage.split("~")[1]

			print(f"[{username}] {content}")
		else:
			print("Massage received from the client is empty")

def send_massage_to_server(client):

	while True:
		massage = input("Massage: ")
		if massage != '':
			client.sendall(massage.encode())
		else:
			print("Empty massage")
			exit(0)

def communicate_to_server():
	username = input("Enter username: ")

	if username != '':
		client.sendall(username.encode())
	else:
		print("Username cannot be empty")
		exit(0)

	threading.Thread(target=listen_for_massages_from_server, args = (client, )).start()

	send_massage_to_server(client)


def main():
	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	try:
		client.connect((HOST, PORT))
		print("Successfuly connected to the server")

	except socket.error as e:
		print(f"Unable to connect to server {HOST} {PORT}: {e}")
		exit(1)

	communicate_to_server()
	client.close()

if __name__ == '__main__':
	main()