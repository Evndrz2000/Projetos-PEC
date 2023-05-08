def main():
    numeros = []
    while True:
        numero = int(input())
        if numero == 0:
            break
        numeros.append(numero)

    if len(numeros) == 0:
        print()
    else:
        maior = numeros[0]
        menor = numeros[0]
        for numero in numeros:
            if numero > maior:
                maior = numero
            if numero < menor:
                menor = numero
        print(f"{maior}")
        print(f"{menor}")

if __name__ == '__main__':
    main()