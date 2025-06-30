a = int(input('Enter first number\t'))
b = int(input('Enter second number\t'))
print(f'The numbers before swapping are {a} and {b}')
a = a+b
b = a-b
a = a-b
print(f'The swapped numbers are {a} and {b}')