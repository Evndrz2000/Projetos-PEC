def calcular_H(n):
    H = 1
    for i in range(2, n+1):
        H += 1/i
    return H
num = int(input("Digite o valor de n: ").strip())
resultado = calcular_H(num)
print(f"o valor de H é: {resultado:.4f}")
