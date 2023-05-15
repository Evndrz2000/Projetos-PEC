def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

num = int(input("Insira um número inteiro: ").strip())

if num < 0:
    print()
else:
    print(factorial(num))