class Funcionario:

    def __init__(self, nome, endereco, telefone, email):
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone
        self.email = email

    def exibeDados(self):
        return f"Nome: {self.nome} \nEndereco: {self.endereco} \nTelefone: {self.telefone} \nEmail: {self.email}"


class Assistente(Funcionario):

    def __init__(self, nome, endereco, telefone, email, numMatricula):
        super().__init__(nome, endereco, telefone, email)
        self.numMatricula = numMatricula

    def exibeDados(self):
        return f"{super().exibeDados()} \nNúmero matrícula: {self.numMatricula}"
    

