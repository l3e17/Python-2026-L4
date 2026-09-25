n = int(input("Enter a number:"))
if n <=1:
    print("This is not a perfect number")
else:
    sum = 0
    for i in range(1, n//2 +1):
        if n % i == 0:
            sum += i

if sum == n:
    print("This is a perfect number")
else:
    print("This is not a perfect number")