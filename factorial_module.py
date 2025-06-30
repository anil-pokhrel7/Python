def factorial(a):
    if a<0:
        raise ValueError("It is not defined for negative value.")
    elif a==0:
        return 1
    else:
        result = 1
        for i in range(1,a+1):
            result *= i
        return result