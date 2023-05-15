def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

num = int(input("Insira um número: "))

if is_prime(num):
    print(f"True")
else:
    print(f"False")
