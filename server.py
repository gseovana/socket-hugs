import threading
import socket
import random
import struct

HOST = '127.0.0.1'
PORT = 2003

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

author_kind_messages = {}
clients = {}
clients_lock = threading.Lock()

# funcao auxiliar para enviar mensagem com tamanho fixo
def send_message(client, message):
    message = message.encode('utf-8')
    message_length = struct.pack('>I', len(message))
    client.sendall(message_length + message)

# funcao auxiliar para receber mensagem com tamanho fixo
def receive_message(client):
    length_data = client.recv(4) # lê 4 bytes para o tamanho da mensagem
    if not length_data:
        return None
    message_length = struct.unpack('>I', length_data)[0]
    return client.recv(message_length).decode('utf-8')

def receive():
    while True:
        try:
            client, address = server.accept()
            print('Conectado com', str(address))

            try:
                send_message(client, 'NICK')
                nickname = client.recv(1024).decode('utf-8')
                with clients_lock:
                    clients[client] = (nickname, address)

                thread = threading.Thread(target=handle, args=(client,))
                thread.start()
            except Exception as e:
                print(f"ops! um erro ao fazer o handshaking: {e}")
                client.close()
        except Exception as e:
            print(f'ops! ocorreu um erro ao tentar aceitar a conexão: {e}')


def handle(client):
    try:
        with clients_lock:
            nickname, address = clients[client]
        print(f"lidando com cliente {nickname} em {address}")

        while True:
            send_message(client, 'MENU')
            option = receive_message(client).strip()  # strip linhas e espaços em branco

            if option == '1':
                send_message(client, 'KIND_MESSAGE')
                kind_message = receive_message(client)

                send_message(client, 'AUTHOR_KIND_MESSAGES')
                author = receive_message(client)
                if not author:
                    author = "anônimo"

                with clients_lock:
                    author_kind_messages[author] = kind_message

                #print(f"{author} deixou uma mensagem: {kind_message}")
                #send_message(client, 'mensagem salva com sucesso!')
            
            elif option == '2':
                with clients_lock:
                    if author_kind_messages:
                        author, message = random.choice(list(author_kind_messages.items()))
                        random_message = f"mensagem de {author}: {message}"
                    else:
                        random_message = "nenhuma mensagem fofa foi deixada ainda :( \n seja o primeiro a deixar uma!\n"
                    send_message(client, random_message)

            elif option == '3':
                send_message(client, 'saindo... até a próxima!')
                with clients_lock:
                    print(f"o cliente {clients[client][0]} desconectou :(")
                    del clients[client]
                client.close()
                break
            else:
                send_message(client, 'opa! essa opção não existe. tente de novo.')
            
    except Exception as e:
        print(f"ops! ocorreu um erro ao lidar com o cliente: {e}")
        with clients_lock:
            if client in clients:
                print(f"o cliete {clients[client][0]} desconectou :(")
                del clients[client]
        client.close()

print("servidor ouvindo...")
receive()