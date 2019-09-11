from _datetime import datetime

class Time():
    def __init__(self, path, mode='rt'):
        self.path = open(path, mode)

    def __enter__(self):
        print('Работаем с файлом и начинаем работу')
        self.time_start = datetime.now()
        print('Время начала работы программы: ', self.time_start)
        return self.path

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.path.close()
        self.time_end = datetime.now()
        print('Закрываем файл\nВремя закрытия программы: ', self.time_end)
        self.time = self.time_end - self.time_start
        print('Время работы программы: ', self.time)


with Time('file.txt', 'w') as file:
    print('Что-то делаем с файлом')
    file.write('Производим действие')