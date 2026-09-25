def get_divisors(n):
    divisors_list=[]#tạo array hứng

    for i in range (1,n+1):
        if n%i==0:
            divisors_list.append(i)
    return divisors_list

k = int(input("Enter a num:"))
print("set of divisors of n:", get_divisors(k))
#2nd way(f"set of ..: {get_divisors(k)}")