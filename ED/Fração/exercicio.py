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

def main():
    while True:
        print("\n=== Menu ===")
        print("1. Criar fração")
        print("2. Realizar operações")
        print("3. Sair")
        opc = input("Escolha uma opção: ")
        if  opc == '1':
            while True:
                try:
                    num = int(input("Digite o numerador da fração: "))
                    den = int(input("Digite o denominador da fração: "))
                    if den <= 0:
                            print("Denominador inválido. O denominador deve ser um número positivo diferente de zero.")
                            continue
                    fraction = Fraction(num, den)
                    print("Fração criada:", fraction)
                    break
                except ValueError:
                    print("Erro: Os numeradores e denominadores devem ser números inteiros.")
        elif  opc == '2':
            if 'fraction' not in locals():
                print("Crie uma fração primeiro.")
                continue
            num2 = int(input("Digite o numerador da segunda fração: "))
            den2 = int(input("Digite o denominador da segunda fração: "))
            fraction2 = Fraction(num2, den2)
            print("Operações:")
            print(f"{fraction} + {fraction2} =", fraction + fraction2)
            print(f"{fraction} - {fraction2} =", fraction - fraction2)
            print(f"{fraction} * {fraction2} =", fraction * fraction2)
            print(f"{fraction} / {fraction2} =", fraction / fraction2)
            print(f"{fraction} > {fraction2}:", fraction > fraction2)
            print(f"{fraction} >= {fraction2}:", fraction >= fraction2)
            print(f"{fraction} < {fraction2}:", fraction < fraction2)
            print(f"{fraction} <= {fraction2}:", fraction <= fraction2)
            print(f"{fraction} == {fraction2}:", fraction == fraction2)
            print(f"{fraction} != {fraction2}:", fraction != fraction2)
        elif  opc == '3':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")



if __name__ == '__main__':
    main()
