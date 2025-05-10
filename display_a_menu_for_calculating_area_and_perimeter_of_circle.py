radius=float(input("Enter the radius of circle: "))
print("1. Calculate perimeter")
print("2. Calculate area")
choise=int(input("Enter the choise(1 or 2): "))
if choise==1:
    area=3.14*radius*radius
    print("Area of circle of radius ",radius,"is",area)
else:
    perimeter=2*3.14*radius
    print("Perimeter of circle of radius ",radius,"is",perimeter)