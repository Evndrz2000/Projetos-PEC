
def celsius(t):
    if t[1] == 'F':
        return (t[0] - 32) * (5/9)
    elif t[1] == 'K':
        return t[0] - 273

    return t[0]

def fahrenheit(t):
    if t[1] == 'C':
        return t[0] * (9/5) + 32
    elif t[1] == 'K':
        return (t[0] - 273) * 1.8 + 32

    return t[0]

def kelvin(t):
    if t[1] == 'C':
        return t[0] + 273
    elif t[1] == 'F':
        return (t[0] - 32) * (5/9) + 273

    return t[0]

def converte_temperatura(valor, base):

    if base == 'C':
        return celsius(valor)
    elif base == 'F':
        return fahrenheit(valor)
    elif base == 'K':
        return kelvin(valor)

def soma_temperaturas(temperaturas):
    soma = 0
    E = temperaturas[1][1]
    for i in temperaturas:
        soma += converte_temperatura(i, E)

    return round(soma, 4), E

def main():
    temperaturas = []
    for _ in range(2):
        t = round(float(input("Insira a temperatura: ")), 4)
        e = input("Insira o índice (°F ou °C): ").upper()[0]
        temperaturas.append((t, e))

    print(soma_temperaturas(temperaturas))

if __name__ == "__main__":
    main()