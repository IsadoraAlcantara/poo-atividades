class Empregado:

    def __init__(self, nomeFuncionario):
        self.nomeFuncionario = nomeFuncionario

    def pagarSalario(self):
        pass


class EmpregadoHora(Empregado):

    def __init__(self, nomeFuncionario, valorHora, horasTrabalhadas):
        super().__init__(nomeFuncionario)
        self.valorHora = valorHora
        self.horasTrabalhadas = horasTrabalhadas

    def pagarSalario(self):
        salario = self.horasTrabalhadas * self.valorHora
        return f"O valor do salário de {self.nomeFuncionario} é R$:{salario}"


class EmpregadoSalario(Empregado):

    def __init__(self, nomeFuncionario, valorSalario):
        super().__init__(nomeFuncionario)
        self.valorSalario = valorSalario

    def pagarSalario(self):
        return f"O valor do salário de {self.nomeFuncionario} é R$:{self.valorSalario}"
    
for empregado in (EmpregadoHora("Luiz", 55, 130), EmpregadoSalario("Catia", 5000)):
    print(empregado.pagarSalario())