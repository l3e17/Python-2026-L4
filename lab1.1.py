import math 
radius = float (input("Enter circle radius:"))
if radius <=0:
    print("Error")
else:
    area = math.pi*(radius**2)
    print(f"Circle area = {area}") # f(f-string) báo hiệu chuỗi đặc biệt vì nó k thể ghi 2 kiểu dữ liệu cộng nhau
