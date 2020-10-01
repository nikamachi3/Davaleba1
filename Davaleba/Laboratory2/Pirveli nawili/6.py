def last_digit(n):
    n = str(n)
    return int(n[len(n)-1])

print(last_digit(int(input("Enter a Number: "))))