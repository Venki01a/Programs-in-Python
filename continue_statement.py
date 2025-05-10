a=b=c=0
n=int(input("Enter the range: "))
for i in range(0,n):
    print("Enter two numbers: ")
    a=int(input("first number: "))
    b=int(input("Second number: "))
    if b==0:
        print("\n The denominator cannot be zero.Enter again !")
        continue
    else:
        c=a//b
        print("Quotient= ",c)