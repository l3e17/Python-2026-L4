def print_student(student):
    print("List of students:")
    for s in student:
       print(f"Student ID: {s.id}, Full name: {s.name}, DoB: {s.dob}")

def print_courses(courses):
    print("List of courses:")
    for c in courses:
        print(f"Course ID: {c.c_id}, Course name: {c.c_name}, Credits: {c.c_credits}")

def print_grade_sheet(student, marks, choose_course):
    print(f"Grade sheet of {choose_course}")
    for s in student:
        std_name = s.name
        std_id = s.id
        course = marks.get(choose_course, {})
        if std_id in course:
            score = course[std_id]
        else:
            score ="none"
        print(f"Name: {std_name}, score: {score}")

def print_sorted_students(student, courses, marks):
    print("\nList of students sorted by GPA descending")
    for s in student:
        gpa = s.get_gpa(courses, marks)
        print(f"Student ID: {s.id}, Name: {s.name}, GPA: {gpa}")

        
