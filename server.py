import socket
import threading
#прописываем порт и ip
PORT = 9090
HOST = "localhost"
#создаем сервер и подключаем tcp, ip
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#делаем адрес
ADDR = (HOST, PORT)
#подключаем к серверу
server.bind(ADDR)
server.listen()
#список клиентов
conns = []

def handle_client(conn, addr):
    try:
     print(f"{addr} connected to server!")
     connected = True
     if connected:
            conn.send(bytes("Write your name:", "utf-8"))
            name = conn.recv(360).decode('utf-8')
            conns.append(conn)
            for c in conns:
                c.send(bytes(name + " joined to the server!", "utf-8"))
                while connected:
                    msg = conn.recv(360).decode('utf-8')

            if msg:
                for c in conns:
                    if c == conn:
                        c.send(bytes('YOU (' + name + '): ' + msg, "utf-8"))
                    else:
                        c.send(bytes(name + ': ' + msg, "utf-8"))
    except:
        for c in conns:
            if c != conn:
                c.send(bytes(f"{name} disconnected!", "utf-8"))
        conn.close()
        print(f"{addr} disconnected!")
        conns.remove(conn)



def start():
    server.listen()
    print("Server is running...")
    while True:
        conn, ADDR = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, ADDR))
        thread.start()


print("Server is starting...")

start()