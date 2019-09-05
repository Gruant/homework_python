from pprint import pprint
def write_dict(cook_book, dish, ingridients):
    cook_book.setdefault(dish, [])
    cook_book[dish].append({'ingridient_name': ingridients[0][0], 'quantity': ingridients[0][1], 'measure': ingridients[0][2]})
    return cook_book

def main():
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
    ingridients = []
    pprint(cook_book)






main()
