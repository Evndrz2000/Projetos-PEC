salario = float(input("Insira o salário: "))
divida = float(input("Insira o valor da dívida: "))
mes = 10
ano = 2016

while divida <= salario:
    if mes == 3:
        salario *= 1.05
    divida *= 1.15
    mes += 1
    if mes == 13:
        mes = 1
        ano += 1

print(f"{mes}/{ano}")
