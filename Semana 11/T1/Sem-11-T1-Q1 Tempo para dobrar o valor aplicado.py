def dobro_juros(d,t):
    q = 0
    valor_atual = d
    seq1 = ''
    while valor_atual < d *2:
        valor_atual += valor_atual * (t / 100)
        q += 1
        
       
        seq1 = str(f"{q}")  
        
    return (f'{seq1}').strip()
def main():
    deposito_inicial = float(input("Insira o deposito inicial: "))
    taxa_juros_anual = float(input("Insira a taxa de juros anual: "))
    qtd = dobro_juros(deposito_inicial, taxa_juros_anual)

    print(f'{qtd}')

if __name__ == '__main__':
    main()
