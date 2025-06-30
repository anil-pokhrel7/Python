def isHappy(n):
    seen = set()

    while n != 1:
        if n in seen:
            return False
            seen.add(n)
        n = sum(int(digit) ** 2 for digit in str(n))

    return True
a = int(input("Enter a number: "))
if isHappy(a):
    print("The number is a happy number.")
elif isHappy(a) == False:
    print("The number is not a happy number.")