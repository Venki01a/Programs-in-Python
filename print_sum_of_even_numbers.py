n=int(input("Enter the number: "))
sum=0
for i in range(1,n):
    if i%2==0:
        sum+=n
        print("Even numbers from 1 to n: ",i)
print("Sum of natural numbers from 1 to n: ",sum)