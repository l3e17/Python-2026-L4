def remove_dollar_sign(s):
    # Thay thế tất cả ký tự "$" bằng chuỗi rỗng ""
    new_string = s.replace("$", "")
    return new_string


ket_qua = remove_dollar_sign("100$ + 50$ = 150$")
print(ket_qua)  
