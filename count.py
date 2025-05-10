a = 'Python is fun'
b = list(a)
count =0
for i in range(len(a)):
    if(a[i]!=' '):
        count +=1
print(count)