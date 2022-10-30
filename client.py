#Сначала нужно понять что входит в функционал
#Функионал создан с отправкой и получением сообщений
import socket
import threading

PORT = 9090

Disconnect_msg = "!DISCONNECT"

SERVER = 'localhost'

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER, PORT))
#отправка
#1.Будет вводиться
#2.Имемет кодировку
#3.Отправка clientom это сообщение
def send_msg():
    msg = input() # ввод сообщения
    message = msg.encode('utf-8') #сообщение = введенное сообщение в кодировке utf-8
    client.send(message) #отправка сообщения
#получение
def recieveMsg():
    print(client.recv(1024).decode())

while True:
    recieveThread = threading.Thread(target=recieveMsg, args=())
    sendThread = threading.Thread(target=send_msg, args=())
    recieveThread.start()
    sendThread.start()

