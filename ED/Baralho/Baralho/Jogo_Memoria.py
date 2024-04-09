from Baralho import Baralho
class JogoDaMemoria:
    def __init__(self):
        self.baralho = Baralho()
        self.baralho.embaralhar()
        self.cartas_viradas = []
        self.pares_encontrados = 0

    def jogar(self):
        while self.pares_encontrados < 26:
            self.mostrar_tabuleiro()
            escolha1, escolha2 = self.ler_escolhas()
            carta1 = self.baralho.cartas[escolha1]
            carta2 = self.baralho.cartas[escolha2]
            self.cartas_viradas.append(carta1)
            self.cartas_viradas.append(carta2)
            if carta1 == carta2:
                print("Par encontrado!")
                self.pares_encontrados += 1
                self.baralho.cartas.pop(escolha1)
                self.baralho.cartas.pop(escolha2)
            else:
                print("Tente novamente!")
            input("Pressione Enter para continuar...")

    def mostrar_tabuleiro(self):
        for i in range(4):
            for j in range(13):
                carta = self.baralho.cartas[i * 13 + j]
                if carta in self.cartas_viradas:
                    print(f"{carta}", end=" ")
                else:
                    print("##", end=" ")
            print()

    def ler_escolhas(self):
        while True:
            try:
                escolha1 = int(input("Digite a posição da primeira carta: "))
                escolha2 = int(input("Digite a posição da segunda carta: "))
                if escolha1 < 0 or escolha1 >= len(self.baralho.cartas):
                    raise ValueError
                if escolha2 < 0 or escolha2 >= len(self.baralho.cartas):
                    raise ValueError
                if escolha1 == escolha2:
                    raise ValueError
                return escolha1, escolha2
            except ValueError:
                print("Entrada inválida. Tente novamente.")


jogo = JogoDaMemoria()
jogo.jogar()

print("Parabéns! Você encontrou todos os pares!")
