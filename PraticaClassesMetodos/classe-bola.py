class Bola:

    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def trocaCor(self, novaCor):
        self.cor = novaCor

    def mostraCor(self):
        return self.cor
    
bola1 = Bola("Amarelo", "20cm", "aço")
print(bola1.mostraCor())
bola1.trocaCor("Azul")
print(bola1.mostraCor())
