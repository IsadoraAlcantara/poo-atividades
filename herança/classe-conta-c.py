class ContaC:

    def __init__(self, numero, saldo, cliente):
        self.__numero = numero
        self.__saldo = saldo
        self.__cliente = cliente

    def creditar(self, valor):
        self.__saldo += valor
        return f"Valor do saldo: {self.__saldo}"
    
    def debitar(self, valor):
        self.__saldo -= valor
        return f"Valor do saldo: {self.__saldo}"
    
    def getSaldo(self):
        return f"Valor do saldo: {self.__saldo}"
    
class CEspecial(ContaC): 

    def __init__(self, numero, saldo, cliente, limite):
        super().__init__(numero, saldo, cliente)
        self.__limite = limite

    def debitar(self, valor):
        self.__saldo -= valor
        return f"Valor do saldo: {self.__saldo} \nLimite da conta: {self.__limite}"

cEspecial1 = CEspecial(2324, 3000, "Isadora", 5000)
print(cEspecial1.debitar(300))