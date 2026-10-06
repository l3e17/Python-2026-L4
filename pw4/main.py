from input import get_course_input, get_marks_input, get_student_input
from output import print_courses, print_grade_sheet, print_sorted_students, print_student

def main():
    student = get_student_input()
    courses, marks = get_course_input()
    choose_course = get_marks_input(student, marks)

    print_student(student)
    print_courses(courses)
    print_grade_sheet(student, marks, choose_course)

    student.sort(key = lambda s : s.get_gpa(courses, marks), reverse=True)

    print_sorted_students(student, courses, marks)

main()