n=int(input("Enter the range: "))
for i in range(1,n):
    print("Element is ",end='')
    print(i)
    if i%2==0:
        break
    else:
        print("Ending loop after printing all elements of sequence")