import math
def compute_distance(x1,y1,x2,y2):
    distance = math.sqrt((x2-x1)**2+(y2-y1)**2)
    return distance

def main_distance():
    print("Điểm A")
    x1 = float(input("Nhập x1:"))
    y1 = float(input("Nhập y1:"))

    print("Diểm B")
    x2 = float(input("Nhập x2:"))
    y2 = float(input("Nhập y2:"))

    result = compute_distance(x1,y1,x2,y2)
    print(f"distance between a and b:{result:.2f}")


main_distance()