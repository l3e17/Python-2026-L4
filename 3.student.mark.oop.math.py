import math 
import numpy as np

student=[]
courses=[]
marks={}#thu vien

num_students = int(input("Enter the number of students:"))
for i in range(num_students):
    print(f"STUDENT {i+1}:")
    s_id = input(" ID: ") #input --- string
    name = input("Full name:")
    dob = input("DOB:")
    infor_std = {
        "id": s_id,
        "name": name,
        "DOB": dob,
    }
    student.append(infor_std) #infor_std is a dictionary so we must use {}

num_courses = int(input("Enter the number of courses"))
for i in range(num_courses):
    print(f"Course {i+1}:")
    c_id = input("ID: ")
    c_name = input("Course name:")
    c_credits = int(input("Enter number of credits:"))#############new
    courses.append ({"c_id": c_id,"course name": c_name, "credits": c_credits})
    marks[c_name] = {}#create a place to keep point of the course #luu y



print("Enter points:")
choose_course = input("Enter the course to enter grade:")
for s in student: # s là biến đại diện để liệt kê ds student
    name_std = s["name"]
    id_std = s["id"]
    raw_score = float(input(f"Nhập điểm cho {name_std}: "))
    score = math.floor(raw_score*10)/10 #16.78 x 10 = 167.8 -> 167 -> 167/10 =16.7#######new
 #Lưu điểm của sinh viên đó vào môn học đã chọn
    marks[choose_course][id_std] = score

###
print("List of courses")
for c in courses:
    id_c = c["c_id"]
    name_c = c["course name"]
    tin_chi = c["credits"]
    print(f"ID: {id_c} , Name: {name_c}, Credits: {tin_chi}" )


print("List of students")
for s in student:
    id_s = s["id"]
    name_s = s["name"]
    Dob = s["DOB"]
    print(f"student id: {id_s}, full name: {name_s}, DoB: {Dob}")

print(F"Grade sheet of {choose_course}")
for s in student:
    std_name = s["name"]
    std_id = s["id"]
#enter the course to find the std score, enter the score sheet of course through marks[choose_course]
    course = marks[choose_course]
    if std_id in course:
        score = course[std_id]
    else:
        score = "chưa có"

    print(f"Name: {std_name}, score: {score}")#####

print("\nList of students sorted by GPA descending")
def get_student_gpa(msv):
    scores = []
    credits = []
    for c in courses:
        ma_mon = c["course name"]
        if ma_mon in marks and msv in marks[ma_mon]:
            scores.append(marks[ma_mon][msv])
            credits.append(c["credits"])

    if len(scores) == 0:##neu sinh vien chua co diem thi tra ve 0
        return 0.0
    #use numpy to calculate
    np_scores = np.array(scores)
    np_credits = np.array(credits)
    gpa = np.dot(np_scores, np_credits) / np.sum(np_credits)
    return math.floor(gpa * 10) / 10
##sap xep
##student.sort(key=lambda s: get_student_gpa(s["id"]), reverse=True)
def lay_tieu_chi_gpa(s):
    return get_student_gpa(s["id"])
student.sort(key=lay_tieu_chi_gpa, reverse=True)#key = (func)
#student dung sort, sort lay tung bộ sv ra truyền vào s(s tự đặt) của laytieuchigpa g, s là một bộ ttin sv. hàm get gpa dc truyền s id là vào lấy id của mỗi sv

for s in student:
    gpa = get_student_gpa(s["id"])
    print(f"Student ID: {s['id']}, Name: {s['name']}, GPA: {gpa}")
