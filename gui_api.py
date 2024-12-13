import requests

import globalvars
import settings
import Network.http_request





def set_repeater_ip_port(ip: str, port: int):
    global settings

    settings.repeater_ip = ip
    settings.repeater_port = port


def get(user_number: str, dns_path: str = None):
    if not dns_path:
        dns_path = "http://"+user_number.split("::")[0]+"/"


    #url = urlparse.urlparse(dns_path)
    req = requests.Request('GET', dns_path)
    _b = Network.http_request.string_from_request(req)
    print("req", _b, "end")
    a = globalvars.connect_and_get(user_number, _b.encode()).decode()
    print("a", a)
    return a
