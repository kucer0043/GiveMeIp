import queue
import socket

import Logger.log
import settings

log_levels = Logger.log.log_levels
logger = Logger.log.Log()
logger.log_level = 999
# somewhere accessible to both:
callback_queue = queue.Queue()




def connect_and_get(ip: str, msg: bytes):
    ip = ip.split("::")
    rep_ip = ip[0].split(":")

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    if not settings.anonizer:
        s.connect((rep_ip[0], int(rep_ip[1])))
    else:
        s.connect((settings.repeater_ip, settings.repeater_port))

    print(1, ip)
    if s.recv(1024) != b'IPvDIY System':
        raise ConnectionError(f"Это не мое")

    splitter = "@_SPEC_@"

    _msg = "SEND" + splitter + ip[1] + splitter



    if settings.anonizer:
        _msg = "ANOSEND".encode() + splitter.encode() + "::".join(ip).encode() + splitter.encode() + _msg.encode() + msg + splitter.encode()
        s.send(_msg)
    else:
        s.send(_msg.encode() + msg + splitter.encode())
    print(2)

    '''if not settings.anonizer:
        _tmp = s.recv(1024)
        if _tmp.decode() != "RECIVE":
            raise ConnectionError(f"Че то не получилось {_tmp}")'''
    print(3)
    return s.recv(4096)