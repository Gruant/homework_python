class Animal():
    
    legs = 0

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
    
    def feed(self):
        print ('Покормили: {}'.format(self.name))

    def setvoice(self, voice):
        self.voice = voice
    
    def howmuchlegs(self, leg):
        self.legs = leg
    

class Goose(Animal):
    def interaction(self):
        print ('Собираем яйца у {}'.format(self.name)) 

class Cow(Animal):
    def interaction(self):
        print ('Доим {}'.format(self.name))

class Sheep(Animal):
    def interaction(self):
        print ('Взяди шерсть с {}'.format(self.name))

class Chicken(Animal):
    def interaction(self):
        print ('Собираем яйца у {}'.format(self.name))

class Goat(Animal):
    def interaction(self):
        print ('Доим {}'.format(self.name))

class Duck(Animal):
    def interaction(self):
        print ('Собираем яйца у {}'.format(self.name))
