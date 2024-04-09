import timeit
import matplotlib.pyplot as plt

def carregar_palavras(nome_arquivo):
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        return arquivo.read().splitlines()

def busca_palavra(palavra, lista_palavras):
    return palavra in lista_palavras

def calcular_tempo_medio_execucao(palavra, lista_palavras, num_execucoes=10):
    tempo_total = timeit.timeit(lambda: busca_palavra(palavra, lista_palavras), number=num_execucoes)
    tempo_medio = tempo_total / num_execucoes
    return tempo_medio * 1e12  # Conversão de segundos para picosegundos

if __name__ == "__main__":
    # Carregar listas de palavras
    palavras_1k = carregar_palavras('palavras1k.txt')
    palavras_10k = carregar_palavras('palavras10k.txt')

    # Palavras a serem pesquisadas
    palavras_pesquisa = ['abacaxi', 'goiaba', 'manga', 'uva', 'zumbu']

    # Calcular tempo médio de busca para cada palavra em cada lista
    resultados_1k = {}
    resultados_10k = {}

    for palavra in palavras_pesquisa:
        tempo_medio_1k = calcular_tempo_medio_execucao(palavra, palavras_1k)
        tempo_medio_10k = calcular_tempo_medio_execucao(palavra, palavras_10k)

        resultados_1k[palavra] = tempo_medio_1k
        resultados_10k[palavra] = tempo_medio_10k
     # Imprimir resultados
    print("Tempo médio de busca para cada palavra em lista de 1000 palavras:")
    for palavra, tempo in resultados_1k.items():
        print(f"{palavra}: {tempo:.2f} picosegundos")

    print("\nTempo médio de busca para cada palavra em lista de 10000 palavras:")
    for palavra, tempo in resultados_10k.items():
        print(f"{palavra}: {tempo:.2f} picosegundos")
    # Plotagem dos resultados
    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.bar(palavras_pesquisa, [resultados_1k[palavra] for palavra in palavras_pesquisa], color='skyblue')
    plt.title('Tempo médio de busca em lista de 1000 palavras')
    plt.xlabel('\n\nPalavras')
    plt.ylabel('Tempo (picosegundos)')

    plt.subplot(1, 2, 2)
    plt.bar(palavras_pesquisa, [resultados_10k[palavra] for palavra in palavras_pesquisa], color='salmon')
    plt.title('Tempo médio de busca em lista de 10000 palavras')
    plt.xlabel('\n\nPalavras')
    plt.ylabel('Tempo (picosegundos)')

    plt.tight_layout()
    plt.show()
