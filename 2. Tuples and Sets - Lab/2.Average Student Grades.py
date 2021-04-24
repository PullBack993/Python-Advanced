def avg(value):
    return sum(value) / len(value)


students_counter = int(input())
students_grades = {}

for _ in range(students_counter):
    student, grade = input().split()
    if student not in students_grades:
        students_grades[student] = []
    students_grades[student].append(float(grade))

for (student, grades) in students_grades.items():
    grades_string = ' '.join(map(lambda grade: f'{grade:.2f}', grades))
    avg_grade = avg(grades)
    print(f'{student} -> {grades_string} (avg: {avg_grade:.2f})')