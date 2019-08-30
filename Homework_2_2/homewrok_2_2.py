class Animal():
    def __init__(self, subanimal, name, weight):
        self.subanimal = subanimal
        self.name = name
        self.weight = weight
    
    def feed(self):
        print ('Покормили: {}'.format(self.name))

    def setvoice(self, voice):
        self.voice = voice
    

class Animal_eggs(Animal):
    def interaction(self):
        print ('Собираем яйца у {}'.format(self.name))

class Animal_milk(Animal):
    def interaction(self):
        print ('Доим {}'.format(self.name))

class Animal_cut(Animal):
    def interaction(self):
        print ('Взяди шерсть с {}'.format(self.name))

class Goose(Animal_eggs):
    pass 

class Cow(Animal_milk):
    pass

class Sheep(Animal):
    pass

class Chicken(Animal_eggs):
    pass

class Goat(Animal_milk):
    pass

class Duck(Animal_eggs):
    pass

a=Goose('Гусь', 'Серый', 15)
b=Goat('Коза', 'Manya', 45)

print(a.weight, b.name)
