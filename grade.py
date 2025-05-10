for i in range(0,100):
    grade=float(input("What\'s the grade percentage? "))
    if grade>=90:
        print("That's an A+ !")
    elif 80<=grade<90:
        print("An A is really good")
    elif 60<=grade:
        print("you got an A-!")
    else:
        print("Fail")