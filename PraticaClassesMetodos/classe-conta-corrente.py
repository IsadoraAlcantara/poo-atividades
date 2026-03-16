class contaCorrente:

    def __init__(self, numConta, nomeCorrentista, saldo = 0):
        self.numConta = numConta
        self.nomeCorrentista = nomeCorrentista
        self.saldo = saldo

    def alterarNome(self, novoNome):
        self.nomeCorrentista = novoNome
        return(f"Nome correntista: {self.nomeCorrentista}")
    
    def deposito(self, valorDeposito):
        self.saldo += valorDeposito
        return(f"Valor saldo: R${self.saldo}")
    
    def saque(self, valorSaque):
        self.saldo -= valorSaque
        return(f"Valor saldo: R${self.saldo}")
    
conta1 = contaCorrente(123, "Isadora", 3000)
print(conta1.alterarNome(input("Informe o novo nome: ")))
print(conta1.deposito(float(input("Informe o valor de deposito: "))))
print(conta1.saque(float(input("Informe o valor de saque: "))))
print(f"Nome: {conta1.nomeCorrentista} \nNúmero conta: {conta1.numConta} \nSaldo: R${conta1.saldo} ")
