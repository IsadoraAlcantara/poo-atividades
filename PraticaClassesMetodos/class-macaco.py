class Macaco:

    alimentos = ["banana", "maçã", "melancia", "ovo", "semente"]

    def __init__(self, nome, bucho=[]):
        self.nome = nome
        self.bucho = bucho

    def comer(self):
        print("Alimentos disponíveis: \n")
        for alimento in self.alimentos:
            print(f"{self.alimentos.index(alimento)} - {alimento}")

        alimentoEscolhido = int(input("\nAlimento escolhido: "))
        self.bucho.append(self.alimentos[alimentoEscolhido])   

    def verBucho(self):
        if self.bucho == []:
            return("\nO bucho está vazio \n")
        else:
            return "\nBucho:\n" + "\n".join(self.bucho)

    def digerir(self):
        self.bucho.clear()
        return("\nO bucho está vazio")
    
macaco1 = Macaco("George")
acao = 1

while acao > 0:
    print(f"\n1 - comer \n2 - ver bucho \n3 - digerir \n")
    acao = int(input(f"O que o {macaco1.nome} vai fazer? "))

    if acao == 1:
        macaco1.comer()

    if acao == 2:
        print(macaco1.verBucho())

    if acao == 3:
        print(macaco1.digerir())