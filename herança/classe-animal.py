class Animal:

    def __init__(self, nome, peso):
        self.nome = nome
        self.peso = peso

    def comer(self, qntGramasComer):
        self.peso += qntGramasComer / 1000
        return f"{self.nome} ganhou {qntGramasComer}, o peso atual é {self.peso}kg"
    
class Cachorro(Animal):

    def __init__(self, nome, peso,):
        super().__init__(nome, peso)

    def latir(self):
        return "\nAu au"
    
class Gato(Animal):

    def __init__(self, nome, peso,):
        super().__init__(nome, peso)

    def miar(self):
        return "\nMiau miau"
    
cachorro1 = Cachorro("Cristal", 3)
gato1 = Gato("Marrie", 2)
acao = 1
while acao > 0:
    animal = int(input("\n1 - cachorro \n2 - gato \nOpção escolhida: "))

    if animal == 1:
        acao = int(input("\n1 - comer \n2 - fazer barulho \n3 - parar programa \nOpção escolhida: "))
        if acao == 1:
            qntComer = int(input(f"Quantidade de gramas que o {cachorro1.nome} vai comer: "))
            print(cachorro1.comer(qntComer))

        elif acao == 2:
            print(cachorro1.latir())
        
        else:
            print("Programa encerrado")
            acao = 0

    elif animal == 2:
        acao = int(input("\n1 - comer \n2 - fazer barulho \n3 - parar programa \nOpção escolhida: "))
        if acao == 1:
            qntComer = int(input(f"Quantidade de gramas que o {gato1.nome} vai comer: "))
            print(gato1.comer(qntComer))

        elif acao == 2:
            print(gato1.miar())
        
        else:
            print("\nPrograma encerrado")
            acao = 0
    
    