cont=0
while True:
    n1 = int(input("Insira um número, ou 0 para finalizar: "))
    cont = cont + n1
    if n1 == 0: break
    
print(f'{cont}')
