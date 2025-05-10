a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
print("Original numbers are ",a,b)
if a>b:
 a,b=b,a
 print("After swapping numbers are ",a,b)
else:
    print("Enter valid inputs")
