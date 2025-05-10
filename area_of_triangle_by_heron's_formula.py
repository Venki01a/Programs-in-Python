import math
a=int(input("Enter the first side: "))
b=int(input("Enter the second side: "))
c=int(input("Enter the third side: "))
s=(a+b+c)/2
area=math.sqrt(s*(s-a)*(s-b)*(s-c))
print("Sides of triangle are ",a,b,c)
print("Area of triangle is ",area)