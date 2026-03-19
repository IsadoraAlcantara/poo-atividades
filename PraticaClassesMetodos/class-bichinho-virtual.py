class BichinhoVirtual:
    comidas = [("pão", 30), ("bife", 50), ("bolo", 20), ("maçã", 10)]

    def __init__(self, nome, fome=100, saude=100, idade=0):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade

    def alterarNome(self, novoNome):
        self.nome = novoNome
        return f"Novo nome {novoNome}"

    def mostrarAtributos(self):
        return f"{self.nome} \nFome: {self.fome} \nSaúde: {self.saude} \nIdade: {self.idade}"

    def mudaFome(self, escolhaAcao):
        if escolhaAcao == 1:
            if self.fome < 10:
                return print(f"{self.nome} não pode brincar agora, está com muita fome")

            else:
                tempoBrincando = int(
                    input(f"Informe quanto tempo o {self.nome} irá brincar (horas): ")
                )
                self.fome -= tempoBrincando * 20
                if self.fome < 0:
                    self.fome = 0

                if self.fome < 20:
                    self.saude = 50
                
            return f"A fome atual do bichinho {self.nome} é {self.fome}"

        elif escolhaAcao == 2:
            print("Oções de comida:\n")
            for comida in self.comidas:
                print(
                    f"{self.comidas.index(comida)} - {comida[0]}, aumenta {comida[1]} da fome"
                )
            escolhaComida = int(input("\nEscolha uma opção, informe o número: "))
            self.fome += self.comidas[escolhaComida][1]
            if self.fome > 100:
                self.fome = 100

            return f"A fome atual do bichinho {self.nome} é {self.fome}"

    def recuperaSaude(self):
        self.saude += 10
        return(f"Saúde: {self.saude}")

    def aumentaIdade(self):
        self.idade += 1
        return(f"Saúde: {self.idade}")

acao = 1
bichinho1 = BichinhoVirtual("Sem nome")

while acao > 0:
    print(f"{bichinho1.mostrarAtributos()} \n")
    acao = int(input("O que deseja fazer: \nMostrar atributos: 1 \nMudar nome: 2 \nBrincar ou comer: 3 \nRecuperar sáude: 4 \nEnvelhecer: 5\nOpção: "))

    if acao == 1:
        print(f"{bichinho1.mostrarAtributos()} \n")

    elif acao == 2:
        print(bichinho1.alterarNome(input("Informe o novo nome: ")))

    elif acao == 3:
        print(bichinho1.mudaFome(int(input(f"O {bichinho1.nome} irá brincar: 1 ou comer: 2? "))))

    elif acao == 4:
        print(bichinho1.recuperaSaude())

    elif acao == 5:
        print(bichinho1.aumentaIdade())
        
