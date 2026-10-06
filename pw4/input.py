import math
from domains.student import Student
from domains.course import Course

def get_student_input():
    student = []
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
        student.append(infor_std)

    return student

def get_course_input():
    courses = []
    marks = {}
    num_courses = int(input("Enter the number of courses"))
    for i in range(num_courses):
        print(f"Course {i+1}:")
        c_id = input("ID: ")
        c_name = input("Course name:")
        c_credits = int(input("Enter number of credits:"))
        courses.append(Course(c_id, c_name, c_credits))
        marks[c_name] = {}
    return courses, marks

def get_marks_input(student, marks):
    print("Enter points:")
    choose_course = input("Enter the course to enter grade:")
    for s in student: # s là biến đại diện để liệt kê ds student
        name_std = s["name"]
        id_std = s["id"]
        raw_score = float(input(f"Nhập điểm cho {name_std}: "))
        score = math.floor(raw_score*10)/10 #16.78 x 10 = 167.8 -> 167 -> 167/10 =16.7#######new
    #Lưu điểm của sinh viên đó vào môn học đã chọn
    marks[choose_course][id_std] = score
    return choose_course
