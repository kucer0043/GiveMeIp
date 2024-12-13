import tkinter as tk
from tkinter import scrolledtext


class MessagingApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Messaging App")

        # Поле для ввода номера пользователя
        self.user_label = tk.Label(master, text="Номер пользователя:")
        self.user_label.pack(pady=5)

        self.user_entry = tk.Entry(master)
        self.user_entry.pack(pady=5)

        # Поле для ввода сообщения
        self.message_label = tk.Label(master, text="Сообщение:")
        self.message_label.pack(pady=5)

        self.message_entry = tk.Entry(master)
        self.message_entry.pack(pady=5)

        # Кнопка для отправки сообщения
        self.send_button = tk.Button(master, text="Отправить", command=self.send_message)
        self.send_button.pack(pady=5)

        # Поле для отображения отправленных сообщений
        self.message_display = scrolledtext.ScrolledText(master, wrap=tk.WORD, height=10, width=40)
        self.message_display.pack(pady=5)
        self.message_display.config(state=tk.DISABLED)  # Запрет редактирования

    def send_message(self):
        user_number = self.user_entry.get()
        message = self.message_entry.get()

        a = callback(user_number, message)
        #self.message_display.insert(tk.END, f"Ответ: {a}\n")

        '''if user_number and message:
            self.message_display.config(state=tk.NORMAL)  # Разрешение редактирования
            self.message_display.insert(tk.END, f"Я: {message}\n")
            self.message_display.config(state=tk.DISABLED)  # Запрет редактирования
            self.user_entry.delete(0, tk.END)  # Очистка поля номера пользователя
            self.message_entry.delete(0, tk.END)  # Очистка поля сообщения'''

    def add_message(self, msg):
        self.message_display.config(state=tk.NORMAL)  # Разрешение редактирования
        self.message_display.insert(tk.END, f"Ответ: {msg}\n")
        self.message_display.config(state=tk.DISABLED)  # Запрет редактирования


root = tk.Tk()
callback = lambda: 2+2
app = MessagingApp(root)


def update(send_msg):
    global callback
    callback = send_msg

    root.update()


def on_msg_get(msg: str):
    print("12421321", msg)
    app.add_message("123123")

