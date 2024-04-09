class Fraction:
    def __init__(self, num=0, den=1):
        self.setNum(num)
        self.setDen(den)

    def getNum(self):
        return self.num

    def getDen(self):
        return self.den

    def setNum(self, num):
        self.num = int(num)

    def setDen(self, den):
        if den <= 0:
            raise ValueError(
                "Denominador inválido. O denominador deve ser um número positivo diferente de zero.")
        self.den = int(den)

    def __str__(self) -> str:
        return f' Fração {self.getNum()}/{self.getDen()}'

    def __add__(self, other):
        if self.getDen() == other.getDen():
            setNum = self.getNum() + other.getNum()
            setDen = self.getDen()
        else:
            setNum = (self.getNum() * other.getDen()) + \
                (self.getDen() * other.getNum())
            setDen = self.getDen() * other.getDen()
        return Fraction(setNum, setDen)

    def __sub__(self, other):
        if self.getDen() == other.getDen():
            setNum = self.getNum() - other.getNum()
            setDen = self.getDen()
        else:
            setNum = (self.getNum() * other.getDen()) - \
                (self.getDen() * other.getNum())
            setDen = self.getDen() * other.getDen()
        return Fraction(setNum, setDen)

    def __mul__(self, other):
        setNum = self.getNum() * other.getNum()
        setDen = self.getDen() * other.getDen()
        return Fraction(setNum, setDen)

    def __truediv__(self, other):
        setNum = self.getNum() * other.getDen()
        setDen = self.getDen() * other.getNum()
        return Fraction(setNum, setDen)

    def __gt__(self, other):
        return (self.getNum() * other.getDen()) > (self.getDen() * other.getNum())

    def __ge__(self, other):
        return (self.getNum() * other.getDen()) >= (self.getDen() * other.getNum())

    def __lt__(self, other):
        return (self.getNum() * other.getDen()) < (self.getDen() * other.getNum())

    def __le__(self, other):
        return (self.getNum() * other.getDen()) <= (self.getDen() * other.getNum())

    def __eq__(self, other):
        return self.getNum() == other.getNum() and self.getDen() == other.getDen()

    def __ne__(self, other):
        return self.getNum() != other.getNum() or self.getDen() != other.getDen()

    def opc_para_selecionar():
        while True:
            print(
                f'-----Menu-----\n1.Soma\n2.Subtração\n3.Multiplicação\n4.Divisão\n5.Sair')
            escolha = input('Digite sua escolha: ')

            if escolha not in ["1", "2", "3", "4", "5"]:
                print("Opção Inválida. Tente Novamente!!!")
                continue
            if escolha == "1":

                while True:
                    try:
                        num1 = int(
                            input("Digite o numerador da primeira fração: "))
                        den1 = int(
                            input("Digite o denominador da primeira fração: "))
                        if den1 <= 0:
                            print(
                                "Denominador inválido. O denominador deve ser um número positivo diferente de zero.")
                            den1 = int(input(
                                "Digite o denominador da primeira fração (deve ser positivo e diferente de zero): "))
                            continue
                        break
                    except ValueError:
                        print(
                            "Erro: Os numeradores e denominadores devem ser números inteiros.")

                while True:
                    try:
                        num2 = int(
                            input("Digite o numerador da segunda fração: "))
                        den2 = int(input("Digite o denominador da segunda fração: "))
                        if den2 <= 0:
                            print(
                                "Denominador inválido. O denominador deve ser um número positivo diferente de zero.")
                            den2 = int(input(
                                "Digite o denominador da segunda fração (deve ser positivo e diferente de zero): "))
                            continue
                        break
                    except ValueError:
                        print(
                            "Erro: Os numeradores e denominadores devem ser números inteiros.")
                fracao = Fraction(num1, den1)
                fracao2 = Fraction(num2, den2)
                resultado = Fraction.soma_fracoes(
                    fracao.getNum(), fracao.getDen(), fracao2.getNum(), fracao2.getDen())
                print(
                    f'Resultado da Soma de {num1}/{den1} + {num2}/{den2} = {resultado}')
                pass

            elif escolha == "2":
                while True:
                    try:
                        num1 = int(
                            input("Digite o numerador da primeira fração: "))
                        den1 = int(
                            input("Digite o denominador da primeira fração: "))
                        if den1 <= 0:
                            print(
                                "Denominador inválido. O denominador deve ser um número positivo diferente de zero.")
                            den1 = int(input(
                                "Digite o denominador da primeira fração (deve ser positivo e diferente de zero): "))
                            continue
                        break
                    except ValueError:
                        print(
                            "Erro: Os numeradores e denominadores devem ser números inteiros.")

                while True:
                    try:
                        num2 = int(
                            input("Digite o numerador da segunda fração: "))
                        den2 = int(
                            input("Digite o denominador da segunda fração: "))
                        if den2 <= 0:
                            print(
                                "Denominador inválido. O denominador deve ser um número positivo diferente de zero.")
                            den2 = int(input(
                                "Digite o denominador da segunda fração (deve ser positivo e diferente de zero): "))
                            continue
                        break
                    except ValueError:
                        print(
                            "Erro: Os numeradores e denominadores devem ser números inteiros.")
                fracao = Fraction(num1, den1)
                fracao2 = Fraction(num2, den2)
                resultado = Fraction.sub_fracoes(
                    fracao.getNum(), fracao.getDen(), fracao2.getNum(), fracao2.getDen())
                print(
                    f'Resultado da Subtração de {num1}/{den1} - {num2}/{den2} = {resultado}')
                pass

            elif escolha == "3":
                while True:
                    try:
                        num1 = int(
                            input("Digite o numerador da primeira fração: "))
                        den1 = int(
                            input("Digite o denominador da primeira fração: "))
                        if den1 <= 0:
                            print(
                                "Denominador inválido. O denominador deve ser um número positivo diferente de zero.")
                            den1 = int(input(
                                "Digite o denominador da primeira fração (deve ser positivo e diferente de zero): "))
                            continue
                        break
                    except ValueError:
                        print(
                            "Erro: Os numeradores e denominadores devem ser números inteiros.")

                while True:
                    try:
                        num2 = int(
                            input("Digite o numerador da segunda fração: "))
                        den2 = int(
                            input("Digite o denominador da segunda fração: "))
                        if den2 <= 0:
                            print(
                                "Denominador inválido. O denominador deve ser um número positivo diferente de zero.")
                            den2 = int(input(
                                "Digite o denominador da segunda fração (deve ser positivo e diferente de zero): "))
                            continue
                        break
                    except ValueError:
                        print(
                            "Erro: Os numeradores e denominadores devem ser números inteiros.")
                fracao = Fraction(num1, den1)
                fracao2 = Fraction(num2, den2)
                resultado = Fraction.multi_fracoes(
                    fracao.getNum(), fracao.getDen(), fracao2.getNum(), fracao2.getDen())
                print(
                    f'Resultado da Multiplicação de {num1}/{den1} * {num2}/{den2} = {resultado}')
                pass


            elif escolha == "4":
                while True:
                    try:
                        num1 = int(
                            input("Digite o numerador da primeira fração: "))
                        den1 = int(
                            input("Digite o denominador da primeira fração: "))
                        if den1 <= 0:
                            print(
                                "Denominador inválido. O denominador deve ser um número positivo diferente de zero.")
                            den1 = int(input(
                                "Digite o denominador da primeira fração (deve ser positivo e diferente de zero): "))
                            continue
                        break
                    except ValueError:
                        print(f"Erro: Os numeradores e denominadores devem ser números inteiros.")

                while True:
                    try:
                        num2 = int(
                            input("Digite o numerador da segunda fração: "))
                        den2 = int(
                            input("Digite o denominador da segunda fração: "))
                        if den2 <= 0:
                            print(
                                "Denominador inválido. O denominador deve ser um número positivo diferente de zero.")
                            den2 = int(input(
                                "Digite o denominador da segunda fração (deve ser positivo e diferente de zero): "))
                            continue
                        break
                    except ValueError:
                        print(
                            "Erro: Os numeradores e denominadores devem ser números inteiros.")
                fracao = Fraction(num1, den1)
                fracao2 = Fraction(num2, den2)
                resultado = Fraction.div_fracoes(
                    fracao.getNum(), fracao.getDen(), fracao2.getNum(), fracao2.getDen())
                print(
                    f'Resultado da Divisão de {num1}/{den1} / {num2}/{den2} = {resultado}')
                pass

            elif escolha == "5":
                break

        print("Obrigado por fazer uso!!!")

if __name__ == '__main__':
    f1 = Fraction()
    f1.opc_para_selecionar()
