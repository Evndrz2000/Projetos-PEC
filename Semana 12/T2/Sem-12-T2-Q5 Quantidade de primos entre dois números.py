def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def prime_numbers(x, y):
    for i in range(x, y+1):
        if is_prime(i):
            print(i)
x = int(input())
y = int(input())
prime_numbers(x, y)