# first of all import the socket library
import random
import socket
import multiprocessing



''' Settings '''

pharse_code = {
    "PEPE": """<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Вы в сети!</title>
    <style>
        body {
            margin: 0;
            padding: 0;
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            background-color: black;
            font-family: Arial, sans-serif;
            color: white;
        }

        h1 {
            font-size: 48px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Вы в сети!</h1>
    </div>
</body>
</html>
"""
}

''' Settings '''


class Client:
    def __init__(self, id: int, c: socket.socket):
        self.id = id
        self.c = c

    def send_and_recive(self, msg: bytes):
        self.c.send(msg)
        return self.c.recv(1024)


def hadle_sender(not_recv, c, clients):
    r = not_recv[1]
    current_user = None
    for i in clients:
        print(r, i.id)
        if r == str(i.id):
            current_user = i
            break

    if not current_user:
        c.send("S404 ERROR".encode())
    else:
        # c.send("RECIVE".encode())
        print("WANЕ SEND")
        print(not_recv[2].encode())
        a = current_user.send_and_recive(not_recv[2].encode())
        print("SENDING")
        print(a)
        c.send(a)
        c.close()

def mr_anonin_sender(msg: str, c):
    if msg[0] != "ANOSEND":
        raise ValueError("И нафига ты меня сюда послал")
    ip = msg[1]

    ip = ip.split("::")
    rep_ip = ip[0].split(":")

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


    s.connect((rep_ip[0], int(rep_ip[1])))

    print(1, ip)
    if s.recv(1024) != b'IPvDIY System':
        return "Это не мой сервак?".encode()

    msg_to_send = "@_SPEC_@".join(msg[2:]).encode()

    print('SENDING ANON', msg_to_send)

    s.send(msg_to_send)
    print(2)
    _tmp = s.recv(1024)
    if _tmp.decode() != "RECIVE":
        return f"Че то не получилось {_tmp}"
    print(3)
    a = s.recv(4096)
    print("get", a)
    c.send(a)


def application(env, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    # next create a socket object
    s = socket.socket()
    print("Socket successfully created")

    port = 8754

    s.bind(('', port))
    print("socket binded to %s" % (port))

    s.listen(100)
    print("socket is listening")

    clients = []

    while True:
        c, addr = s.accept()
        try:
            # Establish connection with client.

            print(type(c))
            print('Got connection from', addr)

            # send a thank you message to the client. encoding to send byte type.
            c.send("IPvDIY System".encode())  # Hello-пакет
            not_recv = c.recv(1024).decode() # Чё надо?
            print(not_recv)
            print("NOT REVCV", not_recv)
            splitter = "@_SPEC_@"
            if splitter in not_recv:
                not_recv = not_recv.split(splitter)
                recv = not_recv[0]
            else:
                recv = not_recv
            print(recv)

            if recv == "CONNECT": # Встаем на связь....
                print("CONNECT", addr)
                print(not_recv[1], addr[0])
                ip = not_recv[1][-4:]
                # ip = random.randint(1000, 2000)
                print(ip)
                clients.append(Client(ip, c))
                # c.send("OK".encode())
                c.send(f"OK {ip}".encode())

            elif recv == "SEND": # Хочу данные....
                print("SEND", addr)
                print("NR", not_recv)
                if not_recv[1] in pharse_code:
                    c.send(f"JR{splitter}{pharse_code[not_recv[1]]}".encode())
                else:
                    mp = multiprocessing.Process(target=hadle_sender, args=(not_recv, c, clients))
                    mp.start()
            elif recv == "ANOSEND":
                print("ANOSEND", addr)
                mp = multiprocessing.Process(target=mr_anonin_sender, args=(not_recv, c))
                mp.start()

            else: # Ты кто?
                c.close()
                print("UNKNOWN", recv)
        except (Exception, BaseException) as e:
            print(e)
            c.close()


if __name__ == '__main__':
    application(None, print)
