def print_pattern(m, n):
    for i in range(m):
        for j in range(n):
            if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                print("*", end=" ")#end=" " để print dc trên 1 hàng nếu k pyhton tự xuống dòng
            else:
                print(" ", end=" ")
        print()


def main_pattern():
    print("--- Vẽ hình chữ nhật rỗng ---")
    hang = int(input("Nhập số hàng (m): "))
    cot = int(input("Nhập số cột (n): "))
    
    
    print_pattern(hang, cot)


main_pattern()
