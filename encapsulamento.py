# 1)
# d) B e C estão corretas

# 2)
class Usuario:

  def __init__(self, primeiroNome):
    self.__primeiroNome = primeiroNome

  def hello(self):
    return(f"Olá, {self.__primeiroNome}")

pessoa1 = Usuario("Joe")
print(pessoa1.hello())

# 3)
class Empregado:

  def __init__(self, nome, salario, projeto):
    self.nome = nome
    self.__salario = salario
    self.projeto = projeto

  def trabalho(self):
    return(f"{self.nome}: {self.projeto}")

  def mostrar(self):
    return(f"{self.nome} e {self.__salario}")


pessoa1 = Empregado("Isadora", "10000", "New Job")
print(pessoa1.trabalho())
print(pessoa1.mostrar())

# 4)
class Robo:

  def __init__(self, nome, anoConstrucao):
    self.__nome = nome
    self.__anoConstrucao = anoConstrucao

  def digaAlo(self):
    return(f"O protótipo {self.__nome} foi criado em {self.__anoConstrucao}")

robo1 = Robo("Anita", "2077")
print(robo1.digaAlo())

# 5)
class Laptop:

  def __init__(self, preco):
    self.__preco = preco

  def getPreco(self):
    return(f"Preço laptop: {self.__preco}")

  def setPreco(self):
    self.__preco = input("Infome o novo preço do laptop: ")
    return(f"Preço laptop: {self.__preco}")


laptop1 = Laptop(300)
print(laptop1.getPreco())
print(laptop1.setPreco())

class Pessoa:

  def __init__(self, primeiroNome, ultimoNome):
    self.__primeiroNome = primeiroNome
    self.__ultimoNome = ultimoNome

  def getPrimeiroNome(self):
    return(self.__primeiroNome)

  def getSegundoNome(self):
    return(self.__segundoNome)

  def setPrimeiroNome(self):
    self.__primeiroNome = input("Informe o primeiro nome: ")

  def setSegundoNome(self):
    self.__segundoNome = input("Informe o segundo nome: ")

pessoa1 = Pessoa("João", "Carvalho")
pessoa1.setPrimeiroNome()
pessoa1.setSegundoNome()
print(f"{pessoa1.getPrimeiroNome()} {pessoa1.getSegundoNome()}")