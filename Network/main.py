import socket
import settings
import GUI.gui_main


class Connection:
    def __init__(self, repeater_ip: str, repeater_port: int, on_get, want_ip: str, on_get_ip):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.connected = False
        self.splitter = "@_SPEC_@"
        self.on_get = on_get
        self.conn_acc = False
        self.r = None
        self.my_ip = ""
        self.want_ip = want_ip
        self.repeater_ip = repeater_ip
        self.repeater_port = repeater_port
        self.on_get_ip = on_get_ip

    def start(self):
        try:
            self.s.connect((self.repeater_ip, self.repeater_port))
        except ConnectionRefusedError as e:
            raise ConnectionRefusedError(f"{e}")

        if self.s.recv(1024).decode() != "IPvDIY System":
            self.close()
            raise ConnectionError("This is not a IPvDIY ip server.")

        self.s.send(f"CONNECT{self.splitter}{self.want_ip}".encode())

    def update(self):
        try:
            recv = self.s.recv(1024)
        except TimeoutError:
            return
        print(recv)
        if self.conn_acc:
            self.r = recv
            self.on_get(recv, self.s.send)
            # self.s.send(b"-")
        if recv.decode() == "OK":
            self.conn_acc = True
            # logger.log("Соединение установлено...")
        elif "OK" in recv.decode():
            d = recv.decode().split(" ")
            if d[0] == "OK":
                print("OKED")
                print(d)
                self.my_ip = f"{self.repeater_ip}:{self.repeater_port}::{d[1]}"
                print(f"YOU IP: ", self.my_ip)
                self.on_get_ip(self.my_ip)
                self.conn_acc = True

    def close(self):
        self.s.close()





def on_get(msg: bytes, send_fn):
    '''s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((settings.my_page_ip, settings.my_page_port))
    s.sendall(msg)
    #print(msg.decode())
    #GUI.debug.on_msg_get(msg.decode())


    send_fn(s.recv(4096))

    print("SENDED")
    s.recv(4096)'''

    print('ME ASK')
    send_fn(b"<h1>BANANCHIKI</h1>213")




def on_get_ip(ip: str):
    GUI.gui_main.window.set_ip_label_text(f"Ваш айпи: {ip}")


network = Connection(settings.repeater_ip, settings.repeater_port, on_get, f"{settings.want_ip}", on_get_ip)
# network = test()
print("IDDDD", id(network))

# GUI.gui_main.network = network