def remover_iguais(lista: list):
    a = []
    for b in lista:
        if b not in a:
            a.append(b)
    return a

def main():
    lista = []
    for _ in range(20):
        lista.append(int(input('Insira um número: ')))

    lista_sem_repetidos = remover_iguais(lista)
    print(lista_sem_repetidos)
    pass

if __name__ == "__main__":
    main()
