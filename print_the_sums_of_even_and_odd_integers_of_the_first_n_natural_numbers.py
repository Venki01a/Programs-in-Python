n=int(input("Enter the last natural number: "))
i=1
sum_even=0
sum_odd=0
while i<=n:
    if i%2==0:
        sum_even+=i
    else:
        sum_odd+=i
    i=i+1
print("Sum of even integers is",sum_even)
print("Sum of odd integers is",sum_odd)