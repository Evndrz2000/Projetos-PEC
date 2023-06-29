def maior_e_menor(matriz):
    maior = float('-inf')
    menor = float('inf')
    posicao_menor = (0, 0)
    posicao_maior = (0, 0)
    for linha in range(len(matriz)):
        for coluna in range(len(matriz[linha])):
            if matriz[linha][coluna] < menor:
                menor = matriz[linha][coluna]
                posicao_menor = (linha, coluna)
            if matriz[linha][coluna] > maior:
                maior = matriz[linha][coluna]
                posicao_maior = (linha, coluna)
    return f'{posicao_maior}\n{posicao_menor}'

def main():
    x = int(input("Digite o valor de X: "))
    matriz_um = []
    for i in range(x):
        a = []
        for j in range(x):
            a.append(int(input("Digite um número: ")))
        matriz_um.append(a)
    print(maior_e_menor(matriz_um))

if __name__ == '__main__':
    main()
