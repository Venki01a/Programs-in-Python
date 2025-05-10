n=int(input("Enter the range: "))
print("The loop with 'break' produces output as : ")
for i in range(1,n):
    if i%3==0:
        break
    else:
        print(i)
        
print("The loop with 'continue' produces output as : ")
for i in range(1,n):
    if i%3==0:
        continue
    else:
        print(i)