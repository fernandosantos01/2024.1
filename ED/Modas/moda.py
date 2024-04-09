def calcular_moda(conjunto):
    contagem = {}
    for elemento in conjunto:
        if elemento in contagem:
            contagem[elemento] += 1
        else:
            contagem[elemento] = 1
    
    modas = []
    max_ocorrencias = max(contagem.values())
    for elemento, ocorrencias in contagem.items():
        if ocorrencias == max_ocorrencias:
            modas.append(elemento)
    
    return modas, max_ocorrencias

def verificar_modalidade(conjunto):
    modas, max_ocorrencias = calcular_moda(conjunto)
    if len(modas) == 1:
        return "Modal", modas[0], max_ocorrencias
    elif len(modas) > 1:
        return "Multimodal", modas, max_ocorrencias
    else:
        return "Amodal", None, None

def main():
    valores = []
    continuar = True
    
    while continuar:
        valor = input("Digite um valor (ou 'fim' para encerrar): ")
        if valor.lower() == 'fim':
            continuar = False
        else:
            try:
                valor = int(valor)
                valores.append(valor)
            except ValueError:
                print("Por favor, digite um valor inteiro válido.")

    modalidade, moda, ocorrencias = verificar_modalidade(valores)
    
    print("Modalidade do conjunto:", modalidade)
    if modalidade == "Modal":
        print("Valor mais frequente:", moda, "(repete", ocorrencias, "vezes)")
    elif modalidade == "Multimodal":
        print("Valores mais frequentes:", moda, "(repetem", ocorrencias, "vezes)")

if __name__ == "__main__":
    main()
