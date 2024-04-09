from Carta import Carta
import random

class Baralho:
    naipes = ["Copas", "Ouros", "Espadas", "Paus"]
    valores = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]

    def __init__(self):
        self.cartas = [Carta(naipe, valor) for naipe in self.naipes for valor in self.valores]

    def __len__(self):
        return len(self.cartas)

    def __str__(self):
        return f"Baralho com {len(self.cartas)} cartas"

    def embaralhar(self):
        random.shuffle(self.cartas)

    def tirar_carta(self):
        return self.cartas.pop()

    def adicionar_carta(self, carta):
        self.cartas.append(carta)
