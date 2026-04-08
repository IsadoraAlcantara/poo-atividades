class Carro:

    def __init__(self, modeloCarro):
        self.modeloCarro = modeloCarro

    def dirigir(self):
        pass


class CarroGasolina(Carro):

    def __init__(self, modeloCarro):
        super().__init__(modeloCarro)

    def dirigir(self):
        return f"{self.modeloCarro}: ronco e fumaça"


class CarroEletrico(Carro):

    def __init__(self, modeloCarro):
        super().__init__(modeloCarro)

    def dirigir(self):
        return f"{self.modeloCarro}: silêncio e suavidade"


for carro in (CarroGasolina("Corolla"), CarroEletrico("Dolphin")):
    print(carro.dirigir())
