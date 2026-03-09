class Quadrado:

    def __init__(self, tamanhoLado):
        self.tamanhoLado = tamanhoLado

    def mudaTamanhoLado(self, novoTamanhoLado):
        self.tamanhoLado = novoTamanhoLado

    def mostrarTamanhoLado(self):
        return self.tamanhoLado
    
    def calcularArea(self):
        area = self.tamanhoLado * self.tamanhoLado
        return area

quadrado1 = Quadrado(4)

print(quadrado1.mostrarTamanhoLado())
quadrado1.mudaTamanhoLado(8)
print(quadrado1.mostrarTamanhoLado())
print(quadrado1.calcularArea())
        