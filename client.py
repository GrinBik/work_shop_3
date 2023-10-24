import socket
from random import choice
from time import sleep

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 1000)
sock.connect(server_address)

questions = ['Какая сейчас температура за окном?',
             'Какой курс доллара к рублю?',
             'Сколько произведений написал М.Ю. Лермонтов?',
             'Какие нужны ингредиенты для тирамису?',
             'Что такое протокол?']

try:
    while True:
        message = choice(questions)
        print(f'Вопрос: {message}')
        message = message.encode()
        sock.sendall(message)
        answer = sock.recv(1024)
        answer = answer.decode('utf-8')
        print(f'Ответ: {answer}\n')
        sleep(3)
finally:
    sock.close()
