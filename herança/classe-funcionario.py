class Pessoa:

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

class Funcionario(Pessoa):

    def __init__(self, nome, idade, salario):
        super().__init__(nome, idade)
        self.salario = salario

    def aumentoSalario(self, porcentagemAumento):
        self.salario = self.salario * (1 + porcentagemAumento / 100)
        return f"Novo salário {self.salario}"
    
funcionario1 = Funcionario("Isadora", "18", 5000)
print(funcionario1.aumentoSalario(20))