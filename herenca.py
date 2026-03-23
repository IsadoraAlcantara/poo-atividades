# modificador | classe mãe | classe filha | escopo global
# protected   | sim        | sim          | não
# private     | sim        | não          | não

class Usuario():

    def __init__(self, nomeUsuario):
        self.__nomeUsuario = nomeUsuario

    def definaNome(self, novoNome):
        self.__nomeUsuario = novoNome
        return(f"Novo nome: {self.__nomeUsuario}")
    
class Admin(Usuario):

    def __init__(self, nomeUsuario):
        super().__init__(nomeUsuario)

    def escrevaNome(self):
        return "Admin"
    
    def digaOla(self):
        return "Olá, Admin, "