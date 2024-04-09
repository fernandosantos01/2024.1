from Carta import Carta
import random
class Baralho:
    def __init__(self):
        naipes = ("Copas", "Ouros", "Espadas", "Paus")
        valores = ("Ás", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Valete", "Dama", "Rei")
        self.cartas = [Carta(naipe, valor) for naipe in naipes for valor in valores]

    def embaralhar(self):
        random.shuffle(self.cartas)

    def tirar_carta(self):
        return self.cartas.pop()
