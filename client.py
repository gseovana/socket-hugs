import socket
import threading
import queue

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 2003))

input_queue = queue.Queue()

nickname = input("Choose your nickname: ").strip()
if not nickname:
    nickname = "anon"

kind_message = input("Type your cute message: ").strip()
if not kind_message:
    kind_message = "No message provided."

author = input("Type your name as an author (if none is informed, it will be anonymous): ").strip()
if not author:
    author = "anonymous"

def receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == 'NICK':
                client.send(nickname.encode('utf-8'))
            elif message == 'KIND_MESSAGE':
                client.send(kind_message.encode('utf-8'))
            elif message == 'AUTHOR_KIND_MESSAGES':
                client.send(author.encode('utf-8'))
                print(f"Sent author: {author}")  # Debugging line
            else:
                print(message)
        except Exception as e:
            print(f"An error occurred: {e}")
            client.close()
            break

def write():
    while True:
        try:
            # Check if there's input in the queue
            if not input_queue.empty():
                message = f"{nickname}: {input_queue.get()}"
                client.send(message.encode('utf-8'))
        except Exception as e:
            print(f"An error occurred in write: {e}")
            client.close()
            break

def input_handler():
    while True:
        # Get user input and put it in the queue
        user_input = input("")
        input_queue.put(user_input)

# Start a thread for handling user input
input_thread = threading.Thread(target=input_handler, daemon=True)
input_thread.start()

receive_thread = threading.Thread(target=receive, daemon=True)
receive_thread.start()

write_thread = threading.Thread(target=write, daemon=True)
write_thread.start()