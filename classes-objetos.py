# 1)
# a) Uma coleção de variáveis e funções trabalhando com essas variáveis.

# 2)
# a) Um objeto nos dá a capacidade de trabalhar com a classe e ter várias instâncias desta mesma classe.

# 3)
# b) Uma variável dentro de uma classe.

# 4)
# a) Uma função dentro de uma classe.

# 5)
# Nome da classe: Usuario
# Propriedades: firstName, lastName
# Método: hello

class Usuario:
  firstName = ""
  lastName = ""

  def hello(self):
    return "Olá"

usuario1 = Usuario()

usuario1.firstName = "Isadora"
usuario1.lastName = "Alcantara"

print(f"{usuario1.hello()} {usuario1.firstName} {usuario1.lastName}")

usuario2 = Usuario()

usuario2.firstName = "Jane"
usuario2.lastName = "Silva"

print(f"{usuario2.hello()}, {usuario2.firstName} {usuario2.lastName}")