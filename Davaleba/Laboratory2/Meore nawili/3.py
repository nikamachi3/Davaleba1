a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))
n = 0
for i in range(1, min(a, b)+1): 
    if a%i==b%i==0: 
        n+=1
        print("Numbers that have been entered ",n,end=";")
        print()