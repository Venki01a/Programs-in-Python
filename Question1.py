M=int(input("Enter the first number: "))
N=int(input("Enter the second number: "))
if M<N:
    print(M)
else:
    while(M>=N):
        M=M-N
    print(M)     # Bad Method
        