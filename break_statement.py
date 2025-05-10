a=b=c=0
n=int(input("Enter the range: "))
for i in range(1,n):
    a=int(input("Enter the first number: "))
    b=int(input("Enter the second number: "))
    if b==0:
        print("Division by zero error!")
        break
    else:
        c=a//b
        print("Quotient= ",c)
print("Program over!")