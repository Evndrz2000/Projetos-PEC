# Faz a contagem do número de ocorrências de um valor na lista
def contar_ocorrencias(lista, valor):
    contador = 0
    for item in lista:
        if item == valor:
            contador += 1
    return contador

# Faz a leitura da list
lista = []
while True:
    valor = int(input("Insira um número ou insira 0 para finalizar: "))
    if valor == 0:
        break
    lista.append(valor)

# Faz a leitura do valor a ser pesquisado
valor_pesquisado = int(input("Insira o valor a ser pesquisado: "))

# Mostra a lista lida, o valor pesquisado e a quantidade de ocorrências
print("Lista lida:", lista)
print("Valor Pesquisado:", valor_pesquisado)
print("Número de ocorrências:", contar_ocorrencias(lista, valor_pesquisado))
