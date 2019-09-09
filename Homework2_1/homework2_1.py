from pprint import pprint

def print_dict():
    cook_book = dict()
    ingridients = []
    with open('recipes.txt', encoding='UTF-8') as file:
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
    cook_book[dish].append({'ingridient_name': ingridients[0][0], 'quantity': ingridients[0][1], 'measure': ingridients[0][2]})
    return cook_book


def ingridients_list(dishes: list, person_count):
    new_dict = dict()
    cook_book = print_dict()
    for dish in dishes:
        if dish in cook_book:
            for new in cook_book[dish]:
              if new['ingridient_name'] in new_dict:
                new_dict[new['ingridient_name']]['quantity'] += (int(new['quantity']) * person_count)
              else:
                new_dict.setdefault(new['ingridient_name'], {'quantity': (int(new['quantity']) * person_count), 'measure': new['measure']})
        else:
            print(f'Блюда {i} нет в списке')
    return new_dict

def main():
    print('Добро пожаловать в домашнюю работу по к лекции 2.4 «Открытие и чтение файла, запись в файл»')
    print('Для проверки задания №1 нажмите 1\nДля проверки задания №2 нажмите 2')
    command = input('Ваша команда: \n')
    if command == '1':
        print(print_dict())
    elif command == '2':
        dish = map(str, input('Введите названия блюд через запятую(без пробела после запятой): ').split(','))
        persons = int(input('Введите кол-во персон: '))
        pprint(ingridients_list(dish, persons))
    else:
        pprint('Неверная команда')

if __name__ == '__main__':
    main()


