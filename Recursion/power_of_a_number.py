def power(x, n):

    if n != 0:
        return x * power(x, n - 1)
    else:
        return 1
    

number = int(input("Enter the base number to find the power of: "))
exponent = int(input("Enter the exponent of the base number: "))
print(number, "^", exponent, "=", power(number, exponent))