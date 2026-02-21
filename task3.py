def factorial(num):
    fatorial = 1
    while num > 1:
        fatorial *= num
        num -=  1
    return fatorial
n= int(input("enter the number: " ))
print (f"factorial of {n} is: {factorial(n)}")

