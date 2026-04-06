class Empregado:

    def __init__(self, codigo, nome, email, salario = 0):
        self._codigo = codigo
        self._nome = nome
        self._email = email
        self._salario = salario

    def getSalario(self):
        return f"O salário do empregado {self._nome} é {self._salario}"
    
    def aumentoSalario(self, percentual):
        aumento = self._salario * (1 + percentual / 100)
        self._salario += aumento
        return f"Novo salário: {self._salario}\n"

class Chefe(Empregado):

    def __init__(self, codigo, nome, email, salario, beneficio):
        super().__init__(nome, email, salario)
        self.beneficio = beneficio

    def aumentoSalario(self, percentual):
        super().aumentoSalario(percentual)
        return f"Aumento salarial com benefícios: {self._salario + self.beneficio}"

class Estagiario(Empregado):

    def __init__(self, codigo, nome, email, salario, desconto):
        super().__init__(codigo, nome, email, salario)
        self.desconto = desconto

    def aumentoSalario(self, percentual):
        super().aumentoSalario(percentual)
        return f"Aumento salarial com benefícios: {self._salario - self.desconto}"

chefe1 = Chefe(34535, "Isadora", "@gmail", 10000, 500)
estagiario1 = Estagiario(34535, "Luiz", "@gmail", 5000, 300)
print(chefe1.getSalario())
print(estagiario1.getSalario())
print(chefe1.aumentoSalario(30))
print(estagiario1.aumentoSalario(10))