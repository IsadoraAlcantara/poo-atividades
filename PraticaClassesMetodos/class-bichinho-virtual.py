class BichinhoVirtual:

    def __init__(self, nome, fome = 100, saude = 100, idade = 0)
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade

    def mostrarNome(self):
        return("Nome: {self.nome}")

    def alterarNome(self, novoNome):
        self.nome = novoNome
        return(f"Novo nome {novoNome}")
    
    def mudaFome(self, brincar, alimentar):
        if self.mudaFome == 1:
            tempoBrincando = int(input(f"Informe quanto tempo o {self.nome} irá brincar (horas): "))
            self.fome -= tempoBrincando * 10
            return self.fome
        
        elif self.mudaFome == 2:
            self.fome += 

