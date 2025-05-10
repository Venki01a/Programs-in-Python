ch=input("Enter the character: ")
if ch>='A' and ch<='Z':
    print("Entered character is an uppercase character")
elif ch>='a' and ch<='z':
    print("Entered character is an lowercase character")
elif ch>='0' and ch<='9':
    print("You entered a digit")
else:
    print("You entered a special character")    