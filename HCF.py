def find_hcf(x,y):
    while y:
        x,y = y,x%y
    return x

def find_hcf_of_list(numbers):
    if len(numbers)<2:
        print("At least two numbers are required to find HCF.")