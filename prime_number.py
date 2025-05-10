n=int(input("Enter the number: "))
a=int(n/2)+1
for i in range(2,a):
    rem=n%i
    if rem==0:
        print(n,"is not prime number")
        break
else:
    print(n,"is prime number")