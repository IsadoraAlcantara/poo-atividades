# 1)
# c) A palavra-chave self

# 2)
class Usuario():

  def __init__(self, primeiroNome, ultimoNome):
    self.primeiroNome = primeiroNome
    self.ultimoNome = ultimoNome

  def hello(self):
    return(f"Olá, {self.primeiroNome}")

# 3)
pessoa1 = Usuario("Jonnie", "Bravo")

# 4)
print(pessoa1.hello())