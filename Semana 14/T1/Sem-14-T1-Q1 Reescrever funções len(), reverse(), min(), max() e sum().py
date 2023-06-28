# a) len(), que recebe uma lista e retorna número de itens:
def comprimento(lista):
    contador = 0
    for item in lista:
        contador += 1
    return contador

# b) reverse(), que recebe uma lista e retorna uma lista com os itens na ordem invertida:
def inverter(lista):
    lista_invertida = []
    for i in range(len(lista)-1, -1, -1):
        lista_invertida.append(lista[i])
    return lista_invertida

# c) min(),que recebe uma lista e retorna o menor valor:
def minimo(lista):
    menor_valor = lista[0]
    for item in lista:
        if item < menor_valor:
            menor_valor = item
    return menor_valor

# d) max(), que recebe uma lista retorna o maior valor:
def maximo(lista):
    maior_valor = lista[0]
    for item in lista:
        if item > maior_valor:
            maior_valor = item
    return maior_valor

# e) sum(), que recebe uma lista retorna a soma dos valores:
def soma(lista):
    soma_total = 0
    for item in lista:
        soma_total += item
    return soma_total

# Leitura dos valores pelo teclado
lista = []
while True:
    valor = int(input("Digite um valor ou 0 para encerrar: "))
    if valor == 0:
        break
    lista.append(valor)

# Mostra a lista lida
print("Lista:", lista)

# Calcula e mostra o resultado de cada função
print("Comprimento da lista:", comprimento(lista))
print("Lista invertida:", inverter(lista))
print("Valor mínimo:", minimo(lista))
print("Valor máximo:", maximo(lista))
print("Soma dos valores:", soma(lista))
