def media_final():
    soma = 0
    quantidade = 0

    while True:
        numero = int(input())
        if numero == 0:
            break
        soma += numero
        quantidade += 1

    if quantidade > 0:
        media = soma / quantidade
        return media
    else:
        return None

def main():
    resultado = media_final()

    if resultado is not None:
        print(f"{resultado:.2f}")
    else:
        print()

if __name__ == '__main__':
    main()
