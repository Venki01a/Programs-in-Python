a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
remainder=a%b
if remainder==0:
    print(a,"is divisible by ",b)
else:
    print(a,"is not divisible by ",b)
    