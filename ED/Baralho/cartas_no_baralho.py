import random

class Carta:
    def __init__(self, valor, naipe):
        self.valor = valor
        self.naipe = naipe

    def __str__(self):
        return f"{self.valor} de {self.naipe}"

class Baralho:
    naipes = ['Copas', 'Paus', 'Espadas', 'Ouros']
    valores = ['Ás', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Valete', 'Dama', 'Rei']

    def __init__(self):
        self.cartas = [Carta(valor, naipe) for naipe in self.naipes for valor in self.valores]

    def embaralhar(self):
        random.shuffle(self.cartas)

    def dar_carta(self):
        if len(self.cartas) > 0:
            return self.cartas.pop()
        else:
            return None

class JogoDeCartas:
    def __init__(self):
        self.baralho = Baralho()
        self.baralho.embaralhar()

    def jogar(self):
        carta_jogador = self.baralho.dar_carta()
        carta_computador = self.baralho.dar_carta()

        if carta_jogador is not None and carta_computador is not None:
            print(f"Você tirou a carta: {carta_jogador}")
            print(f"O computador tirou a carta: {carta_computador}")

            valor_jogador = Baralho.valores.index(carta_jogador.valor)
            valor_computador = Baralho.valores.index(carta_computador.valor)

            if valor_jogador > valor_computador:
                print("Você venceu!")
            elif valor_jogador < valor_computador:
                print("O computador venceu!")
            else:
                print("Empate!")
        else:
            print("Não há cartas suficientes para jogar.")

# Exemplo de uso:
jogo = JogoDeCartas()
jogo.jogar()
