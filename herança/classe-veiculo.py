class Veiculo:

    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def getVeiculo(self):
        return f"Marca: {self.marca} \nModelo: {self.modelo} \nAno {self.ano}"


class Carro(Veiculo):

    def __init__(self, marca, modelo, ano, quantidadePortas):
        super().__init__(marca, modelo, ano)
        self.quantidadePortas = quantidadePortas

    def getCarro(self):
        return f"{self.getVeiculo()} \nQuantidade portas: {self.quantidadePortas}"


class Moto(Veiculo):

    def __init__(self, marca, modelo, ano, cilindradas):
        super().__init__(marca, modelo, ano)
        self.cilindradas = cilindradas

    def getMoto(self):
        return f"{self.getVeiculo()} \nCilindradas: {self.cilindradas}"

veiculo1 = Veiculo("Renault", "Sandero", 2019)
carro1 = Carro("Fiat", "Cronos", 2024, 4)
moto1 = Moto("Marca legal", "Motinho", 2024, 2)
print(f"{veiculo1.getVeiculo()}\n")
print(f"{carro1.getCarro()}\n")
print(f"{moto1.getMoto()}\n")