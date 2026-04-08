class Animal:

    def __init__(self, nomeAnimal):
        self.nomeAnimal = nomeAnimal

    def falar(self):
        pass

class Gato(Animal):

    def __init__(self, nomeAnimal):
        super().__init__(nomeAnimal)

    def falar(self):
        return f"{self.nomeAnimal} diz miau miau"
    
class Cachorro(Animal):

    def __init__(self, nomeAnimal):
        super().__init__(nomeAnimal)

    def falar(self):
        return f"{self.nomeAnimal} diz au au"
    
class Peixe(Animal):

    def __init__(self, nomeAnimal):
        super().__init__(nomeAnimal)

    def falar(self):
        return f"{self.nomeAnimal} diz blub blub"
    
for animal in (Gato("Marrie"), Cachorro("Cristal"), Peixe("Nemo")):
    print(animal.falar())