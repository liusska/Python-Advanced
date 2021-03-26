n = int(input())
students_grade = {}

for _ in range(n):
    [student, grade] = input().split(" ")
    if student not in students_grade:
        students_grade[student] = []
    students_grade[student].append(float(grade))

for (key, value) in students_grade.items():
    avg = sum(value) / len(value)
    values_str = ' '.join(f"{val:.2f}" for val in value)
    print(f"{key} -> {values_str} (avg: {avg:.2f})")