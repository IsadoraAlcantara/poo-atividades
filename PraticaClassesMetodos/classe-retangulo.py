import math
class Retangulo:

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def mudarLador(self):
        selecaoLado = int(input("Informe qual lado você quer mudar, base = 0, altura = 1: "))
        resultado = self.mudarLador(self.altura) if selecaoLado == 1 else self.mudarLador(self.base)
        return resultado
    
    def mostrarLados(self):
        return(f"Base: {self.base} \nAltura: {self.altura}")
    
    def calcularArea(self):
        area = self.base * self.altura
        return area
    
    def calcularPerimetro(self):
        perimetro = self.base * 2 + self.altura

local1 = Retangulo(int(input("Informe a base do local: ")), int(input("Informe a altura do local: ")))
piso1 = Retangulo(int(input("Informe a base do piso: ")), int(input("Informe a altura do piso: ")))

areaPiso = piso1.calcularArea()
areaLocal = local1.calcularArea()
totalPisosAUsar = areaLocal / areaPiso

print(f"área do piso: {areaPiso}m² \n área do local: {areaLocal}2² \n Quantidade total de pisos para cobrir o local: {math.ceil(totalPisosAUsar)} pisos")