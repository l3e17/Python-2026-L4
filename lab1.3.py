num = -1 #mồi để while chạy
while num <=0:
    num = int(input("Enter a number:"))
    if num <= 0:
        print("Error")

        
is_prime = True
if num <=1:
    is_prime = False
else:
    #chia từ 2 đến căn bậc hai của num nếu có số nào chia có dư =0 thì false
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

if is_prime:#k cần viết =true vì if sẽ check dkien sau no la true thí se chay
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")

