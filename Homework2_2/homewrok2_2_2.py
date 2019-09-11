from pprint import pprint
from datetime import datetime, timedelta


class OpenFile():

    def __init__(self, path, mode='rt'):
        self.path = open(path, mode)

    def __enter__(self):
        self.time_start = datetime.now()
        return self.path

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.path.close()
        self.time_end = datetime.now()
        self.time = self.time_end - self.time_start
        print(f'Время работы программы {self.time.microseconds} милисекунд\nРезультат:')


def print_dict():
    cook_book = dict()
    ingridients = []
    with OpenFile('recipes.txt', 'r') as file:
        for line in file:
            dish = line.strip()
            person = file.readline().strip()
            while True:
                ingridient = file.readline().strip()
                if ingridient == '':
                    break
                else:
                    ingridients.append(ingridient.replace(' ', '').split('|'))
                    write_dict(cook_book, dish, ingridients)
                    ingridients = []
        return cook_book


def write_dict(cook_book, dish, ingridients):
    cook_book.setdefault(dish, [])
    cook_book[dish].append(
        {'ingridient_name': ingridients[0][0], 'quantity': ingridients[0][1], 'measure': ingridients[0][2]})
    return cook_book


def main():
    print(print_dict())

if __name__ == '__main__':
    main()
