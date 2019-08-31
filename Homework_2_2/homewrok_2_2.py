class Animal():
    feed = 'Не кормили'
    weight = 0

    def __init__(self, name, weight):
        self.name = str(name)
        self.weight = int(weight)

    def feeding(self):
        print ('Покормили: {}'.format(self.name))
        self.feed = 'Животное сыто'

    def __add__(self, other):
        return self.weight + other.weight

    def __gt__(self, other):
        return self.weight > other.weight


class Goose(Animal):
    legs = 2
    voice = 'Кря кря'
    def interaction(self):
        print ('Собираем яйца у {}'.format(self.name)) 

class Cow(Animal):
    legs = 4
    voice = 'Муууу'
    def interaction(self):
        print ('Доим {}'.format(self.name))

class Sheep(Animal):
    legs = 4
    voice = 'Голос овцы'
    def interaction(self):
        print ('Взяди шерсть с {}'.format(self.name))

class Chicken(Animal):
    legs = 2
    voice = 'Голос курицы'
    def interaction(self):
        print ('Собираем яйца у {}'.format(self.name))

class Goat(Animal):
    legs = 4
    voice = 'Голос козы'
    def interaction(self):
        print ('Доим {}'.format(self.name))

class Duck(Animal):
    legs = 2
    voice = 'Кря кря??'
    def interaction(self):
        print ('Собираем яйца у {}'.format(self.name))


goose1, goose2 = Goose('Серый', 3), Goose('Белый', 5)
cow = Cow('Манька', 140)
sheep1, sheep2 = Sheep('Барашек', 30), Sheep('Кудрявый', 29)
chicken1, chicken2 = Chicken('Ко-Ко', 2), Chicken('Кукареку', 2)
goat1, goat2 = Goat('Рога', 23), Goat('Копыта', 25)
duck = Duck('Кряква', 4)
animals = dict(Гусь=[goose1, goose2], Корова=[cow], Овца=[sheep1, sheep2], Курица=[chicken1, chicken2], Коза=[goat1, goat2], Утка=[duck])

def weight():
    print('------------------ Задача про вес -----------------------')
    all_weight = 0
    max_weight = 0
    max_name = str()
    for key, value in animals.items():
        for k in value:
            all_weight += k.weight
            if k.weight > max_weight:
                max_weight = k.weight
                max_name = k.name

    print(f'Общий вес: {all_weight}')
    print(f'Самый тяжелый: {max_name} с весом в {max_weight}')


def main():
    print('Привет. Если хочешь покормить животное, выбери:\nПокормить: p\nСобрать ресурсы с животного: g\n')

    command = input('Ваша команда: ')

    if command == 'p':
        animal_type = str(input('Какое животное хочешь покормить?: '))
        if animal_type in animals:
            ani_name = input('Введите имя животного: ')
            for k in animals[animal_type]:
                if ani_name == k.name:
                    k.feeding()
                    print('Кстати у {} количество ног: {}, а голос: {}'.format(k.name, k.legs, k.voice))
                    print()
                    weight()
                    return

                else:
                    return print('Животного с таким именем нет')
        else:
            return print('Такого животного нет')

    elif command == 'g':
        animal_type = str(input('С кого соберем ресурсы?: '))
        if animal_type in animals:
            ani_name = input('Введите имя животного: ')
            for k in animals[animal_type]:
                if ani_name == k.name:
                    k.interaction()
                    print('Кстати у {} количество ног: {}, а голос: {}'.format(k.name, k.legs, k.voice))
                    print()
                    weight()
                    return

                else:
                    return print('Животного с таким именем нет')
        else:
            return print('Такого животного нет')

    else:
        return print('Неверная команда. Пока!')

if __name__ == '__main__':
    main()











