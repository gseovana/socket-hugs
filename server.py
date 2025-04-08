import threading
import socket

HOST = '127.0.0.1'
PORT = 2003

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

author_kind_messages = {}
clients = {}
clients_lock = threading.Lock()

def handle(client):
    while True:
        try:
            client.send('KIND_MESSAGE'.encode('utf-8'))
            kind_message = client.recv(1024).decode('utf-8')
            print(kind_message)

            client.send('AUTHOR_KIND_MESSAGES'.encode('utf-8'))
            print("Sent request for author name.")
            author = client.recv(1024).decode('utf-8')
            print(f"Received author: {author}")

            if not author:
                author = "anonymous"

            with clients_lock:
                author_kind_messages[author] = kind_message

            print(f"{author} left a message: {kind_message}")
        except:
            with clients_lock:
                print(f"Client {clients[client][0]} disconnected.")
                del clients[client]
            client.close()
            break

def receive():
    while True:
        client, address = server.accept()
        print('Connected with', str(address))

        client.send('NICK'.encode('utf-8'))
        nickname = client.recv(1024).decode('utf-8')
        with clients_lock:
            clients[client] = (nickname, address)
        print(f"Nickname of the client is {nickname}")

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

print("Servidor ouvindo...")
receive()