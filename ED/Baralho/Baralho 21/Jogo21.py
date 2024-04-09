from Baralho import Baralho

class Jogo21:
    def __init__(self):
        self.baralho = Baralho()
        self.baralho.embaralhar()
        self.jogador_mao = []
        self.croupier_mao = []

    def distribuir_cartas_iniciais(self):
        for _ in range(2):
            self.jogador_mao.append(self.baralho.tirar_carta())
            self.croupier_mao.append(self.baralho.tirar_carta())

    def mostrar_mao(self, mao, nome):
        print(f"Mão de {nome}:")
        for carta in mao:
            print(f"- {carta}")
        print(f"Valor total: {self.pontuacao_mao(mao)}")

    def pontuacao_mao(self, mao):
        return sum(carta.valor_pontuacao() for carta in mao)

    def jogador_jogar(self):
        while True:
            escolha = input("Deseja mais uma carta? (s/n): ")
            if escolha.lower() == "s":
                self.jogador_mao.append(self.baralho.tirar_carta())
                self.mostrar_mao(self.jogador_mao, "Jogador")
                if self.pontuacao_mao(self.jogador_mao) > 21:
                    print("Você perdeu!")
                    return False
            else:
                break
        return True
    # Croupier É o profissional de cassino responsável por "pagar" todos os jogos do salão. Só para motivo de duvida do pq do nome da classe.
    def croupier_jogar(self):
        while self.pontuacao_mao(self.croupier_mao) < 17:
            self.croupier_mao.append(self.baralho.tirar_carta())

        self.mostrar_mao(self.croupier_mao, "Croupier")

    def determinar_vencedor(self):
        jogador_pontuacao = self.pontuacao_mao(self.jogador_mao)
        croupier_pontuacao = self.pontuacao_mao(self.croupier_mao)

        if jogador_pontuacao > 21:
            print("Croupier venceu!")
        elif croupier_pontuacao > 21:
            print("Você venceu!")
        elif jogador_pontuacao > croupier_pontuacao:
            print("Você venceu!")
        elif jogador_pontuacao < croupier_pontuacao:
            print("Croupier venceu!")
        else:
            print("Empate!")

    def jogar(self):
        self.distribuir_cartas_iniciais()
        self.mostrar_mao(self.jogador_mao, "Jogador")
        self.mostrar_mao(self.croupier_mao, "Croupier")

        jogador_continua = self.jogador_jogar()

        if jogador_continua:
            self.croupier_jogar()

        self.determinar_vencedor()

jogo = Jogo21()
jogo.jogar()
