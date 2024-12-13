import http.server
import socketserver
import sys

from PySide6 import QtWidgets, QtGui, QtCore
from PySide6.QtCore import QTimer
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import QLineEdit

import gui_api
import settings


######   ###  ###           ##  ##    ###      ####   #######  ######    ######   #####    # #####
 ##  ##   ##  ##            ##  ##   ## ##    ##  ##   ##   #   ##  ##     ##    ##   ##  ## ## ##
 ##  ##    ####             ##  ##  ##   ##  ##        ##       ##  ##     ##    ##          ##
 #####      ##              ######  ##   ##  ##        ####     #####      ##     #####      ##
 ##  ##     ##              ##  ##  #######  ##        ##       ## ##      ##         ##     ##
 ##  ##     ##              ##  ##  ##   ##   ##  ##   ##   #   ## ##      ##    ##   ##     ##
######     ####             ##  ##  ##   ##    ####   #######  #### ##   ######   #####     ####   

#  ##    ##   ##  #####
 ## ##   ###  ##   ## ##
##   ##  #### ##   ##  ##  
##   ##  #######   ##  ##  
#######  ## ####   ##  ##  
#    ##  ##  ###   ## ##
##   ##  ##   ##  #####

#   ##    ##   ##  #####    ######   #######  ###  ###
# #  ##   ###  ##   ## ##    ##  ##   ##   #   ##  ##
# #   ##  #### ##   ##  ##   ##  ##   ##        ####
# #   ##  #######   ##  ##   #####    ####       ##
# ######  ## ####   ##  ##   ## ##    ##         ##
# #   ##  ##  ###   ## ##    ## ##    ##   #     ##
# #   ##  ##   ##  #####    #### ##  #######    ####

def print_installation_message():
    border = "●▬▬▬▬▬▬▬▬▬▬▬▬▬Привет! Путник!▬▬▬▬▬▬▬▬▬▬▬▬▬●"
    message = (
        "░░░░░░░██████╗░███████╗██████╗░░\n"
        "░░██╗░░██╔══██╗██╔════╝██╔══██╗░\n"
        "██████╗██████╔╝█████╗░░██████╔╝░\n"
        "╚═██╔═╝██╔══██╗██╔══╝░░██╔═══╝░░\n"
        "░░╚═╝░░██║░░██║███████╗██║░░░░░░\n"
        "░░░░░░░╚═╝░░╚═╝╚══════╝╚═╝░░░░░░"
    )

    print(border)
    print(message)
    print(border)
    print('Спасибо за установку восхитительный человек!')


def run_server():
    # Генерируем уникальный порт в диапазоне 8000-9000
    # port = random.randint(8000, 9000)
    port = 8094  # Для теств
    handler = http.server.SimpleHTTPRequestHandler

    with socketserver.TCPServer(("", port), handler) as httpd:
        print(f"Запуск сервера на порту {port}...")
        print(f"Успешно запущено на: http://127.0.0.1:{port}/")
        httpd.serve_forever()


def set_style(self):
    self.setStyleSheet("border-radius: 15px;")
    # Настройка фона
    self.setAutoFillBackground(True)
    palette = self.palette()
    palette.setColor(QtGui.QPalette.Window, QtGui.QColor(27, 32, 40))
    self.setPalette(palette)


class AnotherWindow(QtWidgets.QWidget):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window as we want.
    """

    def __init__(self):
        super().__init__()
        set_style(self)
        layout = QtWidgets.QVBoxLayout()
        self.label = QtWidgets.QLabel("Another Window")
        layout.addWidget(self.label)
        self.setLayout(layout)



class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("IPvDIY UI")
        self.setGeometry(100, 100, 1280, 720)
        set_style(self)

        # Установка вертикального компоновщика
        layout = QtWidgets.QVBoxLayout(self)

        # Menu Layout
        self.menu_layout = QtWidgets.QHBoxLayout(self)
        layout.addLayout(self.menu_layout)



        self.anonimus = QtWidgets.QCheckBox("2-х Уровненная Анонимность", self)
        self.anonimus.setStyleSheet("font-size: 18px; padding: 10px; background-color: white;")
        self.anonimus.stateChanged.connect(self.changed)
        self.menu_layout.addWidget(self.anonimus)

        self.server_settings = QtWidgets.QPushButton("🖥", self)
        self.server_settings.setStyleSheet("font-size: 30px; padding: 10px; background-color: white;")
        self.server_settings.clicked.connect(self.server_settings_open)
        self.menu_layout.addWidget(self.server_settings)


        # Layout для URL
        self.url_layout = QtWidgets.QHBoxLayout(self)
        layout.addLayout(self.url_layout)


        # Поле ввода URL
        self.url_input = QtWidgets.QLineEdit(self)
        self.url_input.setPlaceholderText("Введите URL...")
        self.url_input.setText("127.0.0.1:8754::ADMN")
        self.url_input.setStyleSheet("padding: 10px; font-size: 18px; background-color: white;")
        self.url_layout.addWidget(self.url_input)

        # Кнопка перехода
        self.go_button = QtWidgets.QPushButton("Перейти", self)
        self.go_button.setStyleSheet("font-size: 18px; padding: 10px; background-color: white;")
        self.go_button.clicked.connect(self.on_go_button_clicked)
        self.url_layout.addWidget(self.go_button)


        # Where the webpage is rendered.
        self.webview = QWebEngineView()
        # self.webview.load(QUrl("https://www.python.org/"))
        self.webview.setHtml("<h2>Чел привет</h2>")
        self.webview.urlChanged.connect(self.url_changed)
        layout.addWidget(self.webview)

        # URL address bar.
        self.url_text = QLineEdit()

        # Айпи
        self.ip_label = QtWidgets.QLabel("Загрузка...")
        self.ip_label.setAlignment(QtCore.Qt.AlignCenter)
        self.ip_label.setStyleSheet("font-size: 24px; font-weight: bold; color: #FFFFFF;")
        self.ip_label_text = "Подключение..."
        layout.addWidget(self.ip_label)

        '''# Заголовок
        self.title_label = QtWidgets.QLabel("Введите URL:")
        self.title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.title_label.setStyleSheet("font-size: 24px; font-weight: bold; color: #FFFFFF;")
        layout.addWidget(self.title_label)'''

        # Установка компоновщика
        self.setLayout(layout)


        # Окно с Сервером

        self.server_window = AnotherWindow()


        # Тимер
        self.timer = QTimer()
        self.timer.timeout.connect(self.update)
        self.timer.start(1000)

    def on_go_button_clicked(self):
        url = self.url_input.text()
        if url:
            html = gui_api.get(url)
            self.webview.setHtml(html)
            pass

    def url_changed(self, url):
        """Refresh the address bar"""
        self.url_text.setText(url.toString())

    def update(self):
        self.ip_label.setText(f"{self.ip_label_text}")

    def changed(self, state):
        if int(state) == 0:
            state = False
        elif int(state) == 2:
            state = True
        else:
            raise ValueError("Как ты умудрился поставить галочку в среднее положение")

        settings.anonizer = state

    def server_settings_open(self):
        self.server_window.show()

    def set_ip_label_text(self, a: str):
        self.ip_label_text = a


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()


def start():
    global app, window
    print_installation_message()

    # Запускаем сервер в отдельном потоке
    import threading
    server_thread = threading.Thread(target=run_server, daemon=True)
    server_thread.start()

    # Создаем и запускаем интерфейс

    window.show()

    sys.exit(app.exec())


def update():
    window.show()


if __name__ == '__main__':
    start()
