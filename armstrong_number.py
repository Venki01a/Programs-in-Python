rem=0
arm=0
n=int(input("Enter the number: "))
rem=n%10
arm=arm + (rem*rem*rem)
n=n/10
if arm==n:
    print("Given number is armstrong number")
else:
    print("Given number is not armstrong number")