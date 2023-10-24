import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 1000)
sock.bind(server_address)
sock.listen(1)

while True:
    connection, client_address = sock.accept()
    try:
        while True:
            data = connection.recv(1024)
            if data:
                data = data.decode('utf-8')
                print(f'Вопрос: {data}')
                if data == 'Какая сейчас температура за окном?':
                    answer = 'Сейчас за окном +21 °C.'
                elif data == 'Какой курс доллара к рублю?':
                    answer = '1 доллар США равен 93,50 Российскому рублю.'
                elif data == 'Сколько произведений написал М.Ю. Лермонтов?':
                    answer = 'За свою жизнь Лермонтов успел написать около трех десятков поэм,' \
                             ' примерно 400 стихотворений, а также ряд прозаических и драматических произведений.'
                elif data == 'Какие нужны ингредиенты для тирамису?':
                    answer = '''Необходимы следующие ингредиенты:
- 6 куриных яиц
- 4 столовые ложки сахара
- 500г маскарпоне
- 1 маленькая щепотка соли
- 300мл эспрессо
- 30мл кофейного ликера
- 250г печенья
- 2 столовые ложки какао или тертого шоколада'''
                elif data == 'Что такое протокол?':
                    answer = 'Протоколом называется набор правил, задающих форматы сообщений и процедуры,' \
                             ' которые позволяют компьютерам и прикладным программам обмениваться информацией.'
                print(f'Ответ: {answer}\n')
                connection.send(answer.encode())
    finally:
        connection.close()
