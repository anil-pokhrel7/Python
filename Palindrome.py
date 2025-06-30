def is_palindrome(a):
    return str(a) == str(a)[::-1]

x = int(input("Enter a number to check if the number is palindrome.\t"))
b = is_palindrome(x)
if b == True:
    print(f"{x} is a palindrome number.")
else:
    print(f'{x} is not a palindrome number.')