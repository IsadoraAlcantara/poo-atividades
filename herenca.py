# modificador | classe mãe | classe filha | escopo global
# protected   | sim        | sim          | não
# private     | sim        | não          | não

class Usuario():

    def __init__(self, nomeUsuario):
        self._nomeUsuario = nomeUsuario

    def definaNome(self, novoNome):
        self._nomeUsuario = novoNome
        return(f"Novo nome: {self._nomeUsuario}")
    
    def getNome(self):
        return(f"Nome usuário: {self._nomeUsuario}")
    
class Admin(Usuario):

    def __init__(self, nomeUsuario):
        super().__init__(nomeUsuario)

    def escrevaNome(self):
        return "Admin"
    
    def digaOla(self):
        return(f"Olá Admin, {self._nomeUsuario}")
    
admin1 = Admin("Baltazar")
print(admin1.getNome())