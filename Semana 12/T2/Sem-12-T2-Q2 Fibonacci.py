n = int(input("Insira um número inteiro maior ou igual a 2: "))

a = 0
b = 1

fibo = str(a)

for i in range(n-1):
    c = a + b
    fibo += ", " + str(b)
    a = b
    b = c

print("A constante de Fibonacci é: ",fibo)
