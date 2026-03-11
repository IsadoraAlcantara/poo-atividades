class Pessoa:

    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self):
        self.idade += 1
        if self.idade < 21:
            self.altura += 0.5
        return f"{self.nome} evelheceu 1 ano"

    def engordar(self, maisPeso):
        self.peso += maisPeso
        return f"{self.nome} está com {self.peso}kg"

    def emagracer(self, menosPeso):
        self.peso -= menosPeso
        return f"{self.nome} está com {self.peso}kg"

    def crescer(self, maisAltura):
        self.altura += maisAltura
        return f"{self.nome} está com {self.altura}cm"


pessoa1 = Pessoa("Luiz", 20, 61, 160)

print(pessoa1.envelhecer())
print(pessoa1.engordar(float(input("kg a mais: "))))
print(pessoa1.emagracer(float(input("kg a menos: "))))
print(pessoa1.crescer(float(input("cm a mais: "))))
print(f"{pessoa1.nome} está com {pessoa1.idade} anos, {pessoa1.peso}kg e {pessoa1.altura}cm de altura")
