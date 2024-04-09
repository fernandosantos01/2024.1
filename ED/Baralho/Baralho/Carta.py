class Carta:
    def __init__(self, naipe, valor):
        self.naipe = naipe
        self.valor = valor

    def __str__(self):
        return f"{self.valor} de {self.naipe}"

    def __repr__(self):
        return f"Carta({self.naipe}, {self.valor})"

    def __eq__(self, other):
        return self.naipe == other.naipe and self.valor == other.valor
