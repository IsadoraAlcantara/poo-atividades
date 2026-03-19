class Funcionario:

    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def mostrarNome(self):
        return(f"Nome: {self.nome}")
    
    def mostrarSalario(self):
        return(f"Salário: {self.salario}")
    
    def aumentarSalario(self, percentualAumento):
        self.salario = self.salario * (1 + percentualAumento / 100)
        return(f"Salário: {round(self.salario, 2)}")
        
funcionario1 = Funcionario("Isadora", 10000)
acao = 1

while acao > 0:
    print(f"\n1 - mostrar nome \n2 - mostrar salario \n3 - aumentar salario \n")
    acao = int(input(f"Informe a sua ação: "))

    if acao == 1:
        print(funcionario1.mostrarNome())

    elif acao == 2:
        print(funcionario1.mostrarSalario())

    elif acao == 3:
        print(funcionario1.aumentarSalario(float(input("Informe a porcentagem de aumento do salario, ex: 50% = 50: "))))