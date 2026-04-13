class ContaBancaria:

    def __init__(self, nomeCliente, valorConta, meses):
        self.nomeCliente = nomeCliente
        self.valorConta = valorConta
        self.meses = meses

    def deposito(self, valorDepositar):
        self.valorConta += valorDepositar
        return f"Saldo conta {valorDepositar}"

    def retirada(self, valorRetirada):
        self.valorConta -= valorRetirada
        return f"Saldo conta {valorRetirada}"

    def montante(self):
        pass


class ContaPoupanca(ContaBancaria):

    def __init__(self, nomeCliente, valorConta, meses, taxaJuros):
        super().__init__(nomeCliente, valorConta, meses)
        self.taxaJuros = taxaJuros

    def montante(self):
        resultado = self.valorConta * (1 + self.taxaJuros * self.meses)
        return f"Resultado do montante é {resultado}"


class ContaCorrente(ContaBancaria):

    def __init__(self, nomeCliente, valorConta, meses, taxaJuros):
        super().__init__(nomeCliente, valorConta, meses)
        self.taxaJuros = taxaJuros

    def montante(self):
        resultado = self.valorConta * (1 + self.taxaJuros * self.meses)
        return f"Resultado do montante é {resultado}"


contaCorrente1 = ContaCorrente("Isadora", 5000, 12, 0.04)
contaPoupanca1 = ContaCorrente("Helena", 5000, 12, 0.08)

for conta in (contaCorrente1, contaPoupanca1):
    print(conta.deposito(float(input("Valor de depoisto: "))))
    print(conta.montante())
