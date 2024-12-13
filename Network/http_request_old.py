import socket
import urllib.parse as urlparse

import settings

CONNECTION_TIMEOUT = 5
CHUNK_SIZE = 1024
HTTP_VERSION = 1.1
CRLF = "\r\n\r\n"

socket.setdefaulttimeout(CONNECTION_TIMEOUT)

headers = {
    "Connection": "close",
    "User-Agent": f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) IPvDIY/{settings.version} Safari/537.36",
    "Accept-Encoding": "identity",
    "Cache-Control": "no-cache"
}



def receive_all(sock, chunk_size=CHUNK_SIZE):
    '''
    Gather all the data from a request.
    '''
    chunks = []
    while True:
        chunk = sock.recv(int(chunk_size))
        if chunk:
            chunks.append(chunk)
        else:
            break
    c = []
    for i in chunk:
        c.append(i.decode())

    return ''.join(c)


def GET(url, headers: dict, **kw):
    kw.setdefault('timeout', CONNECTION_TIMEOUT)
    kw.setdefault('http_version', HTTP_VERSION)

    url = urlparse.urlparse(url)
    msg = f'GET {url.path or "/"} HTTP/{kw.get("http_version")} {CRLF}'

    try:
        if not headers["Host"]:
            headers["Host"] = url.hostname
    except KeyError:
        headers["Host"] = url.hostname

    for i in headers:
        msg += f"{i}: {headers[i]} {CRLF}"

    return msg.encode()


if __name__ == '__main__':
    print(GET('http://www.google.com/', headers))
