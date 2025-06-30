def fibonacci(n):
    if n<=1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
numbers = 10
print('Fibonacci series:')
for i in range(numbers):
    print(fibonacci(i), end='')
