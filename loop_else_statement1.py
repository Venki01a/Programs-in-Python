n=int(input("Enter the range: "))
for i in range(1,n):
    if i%2==0:
        break
    print("Element is ",end='')
    print(i)
else:
    print("Ending loop after printing all elements of sequence")