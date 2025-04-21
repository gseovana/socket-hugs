import socket
import threading
import queue
import struct

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 2003))

input_queue = queue.Queue()


def send_message(client, message):
    message = message.encode('utf-8')
    length = struct.pack('>I', len(message))  # empacota a mensagem em 4 bytes
    client.sendall(length + message)

# função auxiliar para receber mensagem com tamanho fixo
def receive_message(client):
    length_data = client.recv(4)  # lê 4 bytes para o tamanho da mensagem
    if not length_data:
        return None
    length = struct.unpack('>I', length_data)[0]  # desempacota o tamanho da mensagem
    message = client.recv(length).decode('utf-8') # lê a mensagem com o tamanho especificado

    return message

def receive():
    while True:
        try:
            message = receive_message(client)
            if not message:
                print("ah não... a conexão foi encerrada pelo servidor >:(")
                client.close()
                break
            if message == 'saindo... até a próxima!':
                print(message)
                client.close()
                break
            if message == 'NICK':
                nickname = input("escolha um nick legal: ").strip()
                if not nickname:
                    nickname = "anon"
                send_message(client, nickname)
            elif message == 'MENU':
                print("----- MENU -----\n")
                print("Escolha uma opção:\n1. Deixar uma mensgaem fofa!\n2. Ler uma mensagem fofa aleatória.\n3. Sair")
                user_input = input("Sua escolha: ")
                send_message(client, user_input)
            elif message == 'KIND_MESSAGE':
                kind_message = input("Digite sua mensagem fofa: ").strip()
                if not kind_message:
                    kind_message = "ué, não tem mensagem?"
                send_message(client, kind_message)
            elif message == 'AUTHOR_KIND_MESSAGES':
                author = input("Informe um autor (você ou outra pessoa. se não informar, será anônimo): ").strip()
                if not author:
                    author = "anônimo"
                send_message(client, author)
                print("mensagem gravada com sucesso!")
            else:
                print(message)
        except Exception as e:
            print(f"ops! ocorreu um erro ao receber a mensagem do server: {e}")
            client.close()
            break

def write():
    while True:
        try:
            if not input_queue.empty():
                message = input_queue.get()
                client.send(message.encode('utf-8'))
        except Exception as e:
            print(f"ah não! um erro ocorreu na função de escrita: {e}")
            client.close()
            break

receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()

receive_thread.join()
write_thread.join()