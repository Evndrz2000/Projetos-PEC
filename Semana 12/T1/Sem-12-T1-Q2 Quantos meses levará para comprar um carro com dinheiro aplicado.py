def main():
    poupanca = 10000
    rendimento = 0.007
    aumento_carro = 0.004

    preco_carro = float(input("Qual é o preço do carro que você quer comprar? "))

    meses = 0
    while poupanca < preco_carro:
        poupanca += poupanca * rendimento
        preco_carro += preco_carro * aumento_carro
        meses += 1

    print(f"Com um rendimento de 0,7% ao mês, em {meses} meses você terá dinheiro para comprar o carro à vista.")

if __name__ == '__main__':
    main()
