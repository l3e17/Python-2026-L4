student=[]
courses=[]
marks={}

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
    courses.append ({"c_id": c_id,"course name": c_name})
    marks[c_name] = {}#create a place to keep point of the course

print("Enter points:")
choose_course = input("Enter the course to enter grade:")
for s in student: # s là biến đại diện để liệt kê ds student
    name_std = s["name"]
    id_std = s["id"]
    
    score = float(input(f"Nhập điểm cho {name_std}: "))
 #Lưu điểm của sinh viên đó vào môn học đã chọn
    marks[choose_course][id_std] = score

###
print("List of courses")
for c in courses:
    id_c = c["c_id"]
    name_c = c["course name"]
    print(f"ID: {id_c} , Name: {name_c}")


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

    print(f"Name: {name}, score: {score}")