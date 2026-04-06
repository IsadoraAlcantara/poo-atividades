class Ingresso:

    def __init__(self, valor):
        self.valor = valor

    def imprimeValor(self):
        return self.valor
    
class VIP(Ingresso):

    def __init__(self, valor, valorAdicional):
        super().__init__(valor)
        self.valorAdicional = valorAdicional

    def imprimeValorVIP(self):
        return super().imprimeValor() + self.valorAdicional
    
class Normal(Ingresso):

    def __init__(self, valor):
        super().__init__(valor)

    def ingressoNormal(self):
        return f"Ingresso normal"
    
class CamaroteInferior(VIP):

    def __init__(self, valor, valorAdicional, localizacaoIngresso, metodoAcessar, metodoImprimir):
        super().__init__(valor, valorAdicional)
        self.localizacaoIngresso = localizacaoIngresso
        self.metodoAcessar = metodoAcessar
        self.metodoImprimir = metodoImprimir

class CamaroteSuperior(VIP):

    def __init__(self, valor, valorAdicional):
        super().__init__(valor, valorAdicional)

camaroteSuperior1 = CamaroteSuperior(200, 50)
print(camaroteSuperior1.imprimeValorVIP())