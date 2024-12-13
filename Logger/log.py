import time

log_levels = {
    "TRACE": -1,
    "DEBUG": 0,
    "INFO": 1,
    "WARNING": 2,
    "ERROR": 3
}


def safe_zero_div(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return 0
def dict_by_value(dict: dict, value):
    return list(dict.keys())[list(dict.values()).index(value)]


class Log:

    def __init__(self):
        self.log_level: int = log_levels["TRACE"]
        self.log_file = open("log.log", "w", encoding="utf-8")
        self.loop_hook = []
        self._last_log = time.time()
        self._old_loop = False
        self._old_not_print = False
        self.first = True
        self.loop_time = 0

    def log(self, message, log_level=log_levels["INFO"], loop=False, out=True, ret_line=False, print_to_console=True):
        """
        Лог в файл

        :param message: Сообщение
        :param log_level: Лог левел (бери из log_levels)
        :param loop: -
        :param out: -
        :param ret_line: -
        :param print_to_console: Выводить ли в консоль?
        :return:
        """
        a = time.time() - self._last_log
        if not self.first:
            write_str = "    Занял {:.4f} с ({:.1f} FPS)\n".format(a, safe_zero_div(1, a))
        else:
            self.first = False
            write_str = "Запуск логов. Время без логов: {:.4f} с\n".format(a)
        if self._old_loop:
            self.loop_time += a

        if self._old_loop:
            if len(self.loop_hook) > 0:
                self.loop_hook[len(self.loop_hook) - 1] += write_str
        else:
            self.log_file.write(write_str)

            if self.log_level <= log_level:
                if not self._old_not_print:
                    print(write_str, end="")
                else:
                    self._old_not_print = False

        if not out:
            return
        if loop:
            loop_add_string = "{LOOP} "
        else:
            loop_add_string = ""

        write_str = f"{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())} {loop_add_string}[{dict_by_value(log_levels, log_level)}]: {message}"
        loop = loop
        if ret_line:
            write_str = "\n" + write_str

        if loop:
            self.loop_hook.append(write_str)
            self._old_loop = loop
            self._last_log = time.time()
            return
        self.log_file.write(write_str)

        if self.log_level <= log_level:
            if print_to_console:
                print(write_str, end="")
            else:
                self._old_not_print = True

        self._old_loop = loop
        self._last_log = time.time()

    def llog(self, message, log_level=log_levels["INFO"]):
        """
        Все тоже самое что и log(), только при кажом цикле стирается.
        :param message: Сообщение
        :param log_level: Лог левел (бери из log_levels)
        :return:
        """
        self.log(message, log_level, loop=True)

    def close(self, msg, level=log_levels["INFO"]):
        self.log_file.writelines(self.loop_hook)
        self.log(msg, level, ret_line=True, print_to_console=False)
        self.log("", level, out=False, print_to_console=False)
        self.log_file.close()

    def loop_clear(self):
        """
        Вызывать при каждой итерации цикла для правильной работы llog()
        :return:
        """
        self.loop_hook = []
        try:
            self.llog("ФПС цикла {:.1f}".format(1 / self.loop_time), log_levels["INFO"])
        except ZeroDivisionError:
            pass
        self.loop_time = 0

