class Fraction:
    def __init__(self, w_num, w_den):
        self.num = w_num
        self.den = w_den
        
    def show(self):
        print(self.num, '/', self.den)

    def __str__(self) -> str:
        return "Fracao: " + str(self.num) + "/" + str(self.den)

    def getNum(self):
        return self.num

    def getDen(self):
        return self.den

    def __add__(self, other):
        new_num = self.num * other.den + other.num * self.den
        new_den = self.den * other.den
        return Fraction(new_num, new_den)

    def __sub__(self, other):
        new_num = self.num * other.den - other.num * self.den
        new_den = self.den * other.den
        return Fraction(new_num, new_den)

    def __mul__(self, other):
        new_num = self.num * other.num
        new_den = self.den * other.den
        return Fraction(new_num, new_den)

    def __truediv__(self, other):
        new_num = self.num * other.den
        new_den = self.den * other.num
        return Fraction(new_num, new_den)

    def __gt__(self, other):
        return self.num / self.den > other.num / other.den

    def __ge__(self, other):
        return self.num / self.den >= other.num / other.den

    def __lt__(self, other):
        return self.num / self.den < other.num / other.den

    def __le__(self, other):
        return self.num / self.den <= other.num / other.den

    def __eq__(self, other):
        return self.num / self.den == other.num / other.den

    def __ne__(self, other):
        return self.num / self.den != other.num / other.den


if __name__ == '__main__':
    f1 = Fraction(7, 3)
    f2 = Fraction(2, 5)

    print(f1.getNum())  # Saída: 7
    print(f1.getDen())  # Saída: 3

    print(f1 + f2)  # Saída: Fracao: 41/15
    print(f1 - f2)  # Saída: Fracao: 29/15
    print(f1 * f2)  # Saída: Fracao: 14/15
    print(f1 / f2)  # Saída: Fracao: 35/6

    print(f1 > f2)  # Saída: True
    print(f1 >= f2)  # Saída: True
    print(f1 < f2)  # Saída: False
    print(f1 <= f2)  # Saída: False
    print(f1 == f2)  # Saída: False
    print(f1 != f2)  # Saída: True
