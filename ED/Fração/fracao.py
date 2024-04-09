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
        self.den = int(den)

    def __str__(self) -> str:
        return f' Fração {self.getNum()}/{self.getDen()}'

    @staticmethod
    def soma_fracoes(num1, den1, num2, den2):
        if den1 == den2:
            setNum = int(num1 * num2)
            setDen = den1
        else:
            setNum = int((num1 * den2) + (den1 * num2))
            setDen = int(den1 * den2)
        return Fraction(setNum, setDen)

    @staticmethod
    def sub_fracoes(num1, den1, num2, den2):
        if den1 == den2:
            setNum = int(num1 * num2)
            setDen = int(den1-den2)
        else:
            setNum = int((num1 * den2) - (den1 * num2))
            setDen = int(den1 * den2)
        return Fraction(setNum, setDen)
    @staticmethod
    def multi_fracoes(num1, den1, num2, den2):
            setNum = int(num1 * num2)
            setDen = int(den1*den2)
            return Fraction(setNum, setDen)
    @staticmethod
    def div_fracoes(num1, den1, num2, den2):
            setNum = int(num1 * den2)
            setDen = int(den1*num2)
            return Fraction(setNum, setDen)
    @staticmethod
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
    # Inicializando com valores iniciais válidos para evitar erros na inicialização
    f1 = Fraction()
    f1.opc_para_selecionar()
