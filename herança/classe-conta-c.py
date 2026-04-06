class ContaC:

    def __init__(self, numero, saldo, cliente):
        self._numero = numero
        self._saldo = saldo
        self._cliente = cliente

    def creditar(self, valor):
        self._saldo += valor
        return f"Cliente: {self._cliente} \nValor do saldo: {self._saldo}"
    
    def debitar(self, valor):
        self._saldo -= valor
        return f"Cliente: {self._cliente} \nValor do saldo: {self._saldo}"
    
    def getSaldo(self):
        return f"Cliente: {self._cliente} \nValor do saldo: {self._saldo}"
    
class CEspecial(ContaC): 

    def __init__(self, numero, saldo, cliente, limite):
        super().__init__(numero, saldo, cliente)
        self.__limite = limite

    def debitar(self, valor):
        self._saldo -= valor
        return f"{super().debitar(valor)} \nLimite da conta: {self.__limite}"
    
class CPoupanca(ContaC):

    def __init__(self, numero, saldo, cliente, saldoMinimo):
        super().__init__(numero, saldo, cliente)
        self.__saldoMinimo = saldoMinimo
    
    
    def atualizarSaldo(self, novoSaldo):
        self._saldo = novoSaldo
        return f"Cliente: {self._cliente} \nNovo saldo: {self._saldo}"
    
    def getSaldoMinimo(self):
        return f"Cliente: {self._cliente} \nNovo saldo: {self.__saldoMinimo}"
    
class CInvestimento(ContaC):

    def __init__(self, numero, saldo, cliente, dataInvestimento, periodo):
        super().__init__(numero, saldo, cliente)
        self.__dataInvestimento = dataInvestimento
        self.__periodo = periodo

    def atualizarSaldo(self, novoSaldo):
        self._saldo = novoSaldo
        return f"Cliente: {self._cliente} \nNovo saldo: {self._saldo}"


cEspecial1 = CEspecial(2324, 3000, "Isadora", 5000)
print(cEspecial1.debitar(300))