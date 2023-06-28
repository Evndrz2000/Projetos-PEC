def positivos(lista):
    positivo = []
    for i in lista:
        if i > 0:
            positivo.append(i)
    return positivo

def negativos(lista):
    negativo = []
    for j in lista:
        if j < 0:
            negativo.append(j)
    return negativo

def soma_positivo(lista):
    a = 0
    for b in lista:
        a += b
    return a

def main():
    lista = []
    for _ in range(10):
        lista.append(int(input('Insira um número: ')))
    print(lista)
    print(len(negativos(lista)))
    print(soma_positivo(positivos(lista)))

    pass

if __name__ == "__main__":
    main()
