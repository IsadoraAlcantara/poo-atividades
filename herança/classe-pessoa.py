class Pessoa:

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def getPessoa(self):
        return(f"Nome pessoa: {self.nome}, idade pessoa: {self.idade}")

class Aluno(Pessoa):

    def __init__(self, nome, idade, nota):
        super().__init__(nome, idade)
        self.nota = nota

    def getAluno(self):
        return(f"Nome aluno: {self.nome}, idade aluno: {self.idade}, nota aluno: {self.nota}")
    
pessoa1 = Pessoa("Ana", 23)
aluno1 = Aluno("Luiz", 50, 7)
print(pessoa1.getPessoa())
print(aluno1.getAluno())