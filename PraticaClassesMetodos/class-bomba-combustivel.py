class BombaCombustivel:

    def __init__(self, tipoCombustivel, valorLitro, qntCombustivel):
        self.tipoCombustivel = tipoCombustivel
        self.valorLitro = valorLitro
        self.qntCombustivel = qntCombustivel

    def abastecerPorValor(self, valorAbastecido):
        qntLitrosAbastecidos = round(valorAbastecido / self.valorLitro, 2)
        return f"Valor a ser abastecido: {valorAbastecido} \nQuantidade litros: {round(qntLitrosAbastecidos, 2)} \n{self.alterarQntCombustivelBomba(qntLitrosAbastecidos)}"

    def abastecerPorLitro(self, qntLitrosAbastecidos):
        return f"Valor a ser abastecido: {qntLitrosAbastecidos * self.valorLitro} \nQuantidade litros: {qntLitrosAbastecidos} \n{self.alterarQntCombustivelBomba(qntLitrosAbastecidos)}"

    def alterarValorCombustivel(self, combustivelNovoValor):
        self.valorLitro = combustivelNovoValor
        return f"Valor combustível: {self.valorLitro}"

    def alterarCombustivel(self, novoTipoCombustivel):
        self.tipoCombustivel = novoTipoCombustivel
        return f"Tipo combustível: {self.tipoCombustivel}"

    def alterarQntCombustivelBomba(self, diminuiQntCombustivel):
        self.qntCombustivel -= diminuiQntCombustivel
        return f"Quantidade de combustível na bomba: {self.qntCombustivel}"


bomba1 = BombaCombustivel("gasolina", 5.5, 50)
acao = 1

while acao > 0:
    print(
        f"\n1 - abastecer por valor \n2 - abastecer por litro \n3 - alterar valor combustível \n4 - alterar combustível"
    )
    acao = int(input(f"\nInforme sua ação: "))

    if acao == 1:
        print(bomba1.abastecerPorValor(float(input("\nInforme o valor a abastecer: "))))

    elif acao == 2:
        print(
            bomba1.abastecerPorLitro(float(input("\nInforme a quantidade de litros: ")))
        )

    elif acao == 3:
        print(
            bomba1.alterarValorCombustivel(float(input("\nNovo valor combustível: ")))
        )

    elif acao == 4:
        print(bomba1.alterarCombustivel(input("\nNovo combustível: ")))
