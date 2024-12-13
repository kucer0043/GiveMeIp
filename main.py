

import GUI.gui_main
from Network import main as net
import multiprocessing




def network_update(network):
    while True:
        network.update()

def gui_action(user_number, message) -> str:
    global network
    net.connect_and_get(user_number, message.encode()).decode()




if __name__ == '__main__':
    #print(gui_api.get_my_ip())
    net.network.start()
    mp = multiprocessing.Process(target=network_update, args=(net.network, ))
    mp.start()
    GUI.gui_main.start()

