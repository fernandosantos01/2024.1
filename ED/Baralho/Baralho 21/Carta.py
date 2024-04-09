class Carta:
    def __init__(self, naipe, valor):
        self.naipe = naipe
        self.valor = valor

    def __repr__(self):
        return f"{self.valor} de {self.naipe}"

    def valor_pontuacao(self):
        if self.valor == "Ás":
            return 11
        elif self.valor in ("Valete", "Dama", "Rei"):
            return 10
        else:
            return int(self.valor)
