class Usuario():

  def __init__(self, primeiroNome, segundoNome):
    self.primeiroNome = primeiroNome
    self.segundoNome = segundoNome

  def getNomeCompleto(self):
    return(f"Seja bem-vindo, {self.primeiroNome} {self.segundoNome}")

pessoa1 = Usuario("Johnny", "Bravo")
print(pessoa1.getNomeCompleto())