from math import pi


class Forma:

    def __init__(self, tipoForma):
        self.tipoForma = tipoForma

    def area(self):
        pass


class Quadrado(Forma):

    def __init__(self, lado):
        super().__init__("quadrado")
        self.lado = lado

    def area(self):
        areaTotal = self.lado**2
        return f"O {self.tipoForma} tem {areaTotal} cm² de área"


class Circulo(Forma):

    def __init__(self, raio):
        super().__init__("círculo")
        self.raio = raio

    def area(self):
        areaTotal = pi * self.raio**2
        return f"O {self.tipoForma} tem {round(areaTotal, 2)} cm² de área"


for forma in (Quadrado(2), Circulo(5)):
    print(forma.area())
