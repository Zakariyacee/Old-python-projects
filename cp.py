class Mammals:
    def __init__(self,animal, sound):
        self.animal = animal
        self.sound = sound

    def makesound(self):
        return self.animal + " goes " + self.sound


class Elephant(Mammals):
    def __init__(self,animal, sound):
        super().__init__(animal, sound)

class Kangaroos(Mammals):
    def __init__(self, animal, sound):
        super().__init__(animal, sound)

    
class Whales(Mammals):
    def __init__(self, animal, sound):
        super().__init__(animal, sound)


listofmammals = [Elephant('elephant','trumpeet'), Kangaroos('kangaroos', 'cough'), Whales('Whales', 'click')]
for animal in listofmammals:
    print(animal.makesound())
