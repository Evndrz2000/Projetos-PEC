def calcular(matriz):
    soma_primeira_linha = sum(matriz[0])
    soma_ultima_coluna = sum([linha[-1] for linha in matriz])
    media = round(sum([sum(linha) for linha in matriz]) / (len(matriz) * len(matriz[0])), 4)
    menor = min([min(linha) for linha in matriz])
    maior = max([max(linha) for linha in matriz])
    return soma_primeira_linha, soma_ultima_coluna, media, menor, maior

def main():
    n = int(input())
    m = int(input())
    matriz = []
    for a in range(n):
        linha = []
        for b in range(m):
            linha.append(int(input()))
        matriz.append(linha)
    z = calcular(matriz)
    print(z)

if __name__=='__main__':
    main()