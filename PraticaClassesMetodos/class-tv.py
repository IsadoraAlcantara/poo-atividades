class Tv:

    def __init__(self, numCanal, volume):
        self.numCanal = numCanal
        self.volume = volume

    def mudaCanal(self, novoCanal):
        if novoCanal >= 1 and novoCanal <= 8:
            self.numCanal = novoCanal
            return f"Canal atual: {self.numCanal}"

        else:
            return "Canal inexistente. Canais disponíveis: 1 à 8"

    def mudaVolume(self, somaVolume):
        if self.volume + somaVolume >= 0 and self.volume + somaVolume <= 100:
            self.volume += somaVolume
            return f"Volume: {self.volume}"

        else:
            return "O volume vai de 0 à 100"


tv1 = Tv(2, 30)
controle = 1

while controle > 0:
    acao = int(
        input(
            "\nInforme a ação desejada: \n1 - muda canal \n2 - muda volume: \n0 - encerra progama\n\nOpção selecionada: "
        )
    )
    controle = acao

    if acao == 1:
        print(tv1.mudaCanal(int(input("\nInforme o canal desejado: "))))

    elif acao == 2:
        print(
            tv1.mudaVolume(int(input("\nInforme o valor de volume a ser alterado: ")))
        )
