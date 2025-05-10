a=int(input("Enter the value of a: "))
b=int(input("Enter the value of b: "))
c=int(input("Enter the value of c: "))
d=int(input("Enter the value of d: "))
if a>b and a>c and a>d:
    print("a is greater")
elif b>c and b>d and b>a:
    print("b is greater")
elif c>d and c>a and c>b:
    print("c is greater")
elif d>a and d>b and d>c:
    print("d is greater")
else:
    print("All are equal")