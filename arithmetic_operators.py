a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
operator=input("Enter the operator[+,-,*,/]: ")
result=0
if operator=='+':
    result=a+b
elif operator=='-':
    result=a-b
elif operator=='*':
    result=a*b
elif operator=='/':
    result==a/b
else:
    print("Invalid operator")
print(a,operator,b,"=",result)