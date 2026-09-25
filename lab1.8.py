def extract_even(l):#hàm lấy số nguyên với biến mẫu là l
    even_list = []#tạo mảng rỗng chauws kqua

    for num in l:
        if num % 2 == 0:
         even_list.append(num)

    return even_list

danh_sach_test = [1,4,5,-1,10]
result = extract_even(danh_sach_test)
print(result)