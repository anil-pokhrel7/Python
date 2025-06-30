def prime(n):
    if n<2:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    else:
        return True
n = int(input("Enter a number\t"))
if prime(n):
    print(f'{n} is a prime number.')
else:
    print(f'{n} is not a prime number.')