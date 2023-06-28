Temperatura = 0
Escala = 1

def ler_temp():
    temp = float(input("Insira a temperatura: "))
    escala = input("Insira a escala (°F ou °C): ").upper()[0]
    return temp, escala

def f_para_c(TF):
    return (TF[Temperatura] - 32) * (5 / 9), 'C'

def temp_maior(T1, T2):
    if T1[Escala] == T2[Escala]:
        return T1 if T1[Temperatura] > T2[Temperatura] else T2
    else:
        if T1[Escala] == 'F':
            aux1 = f_para_c(T1)
            aux2 = T2
        else:
            aux1 = T1
            aux2 = f_para_c(T2)
        return T1 if aux1[Temperatura] > aux2[Temperatura] else T2

def main():
    T1 = ler_temp()
    T2 = ler_temp()

    maior = temp_maior(T1, T2)

    print(maior)

if __name__=='__main__':
    main()
