class ContaInvestimentos:

    def __init__(self, saldoInicial, taxaJuros):
        self.saldoInicial = saldoInicial
        self.taxaJuros = taxaJuros

    def adicioneJuros(self):
        self.saldoInicial *= (1 + self.taxaJuros / 100)
        return(f"Saldo atual: {round(self.saldoInicial, 2)}")
    
conta1 = ContaInvestimentos(1000, 10)
qntVezesTaxaJuros = int(input("Informe a quantidade de vezes que os juros serão somados ao saldo: "))
for i in range(0, qntVezesTaxaJuros):
    print(conta1.adicioneJuros())
