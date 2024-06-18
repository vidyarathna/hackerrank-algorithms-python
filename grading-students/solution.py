def gradingStudents(grades):
    rounded_grades = []
    for grade in grades:
        if grade >= 38:
            next_multiple_of_5 = (grade + 4) // 5 * 5
            if next_multiple_of_5 - grade < 3:
                rounded_grades.append(next_multiple_of_5)
            else:
                rounded_grades.append(grade)
        else:
            rounded_grades.append(grade)
    return rounded_grades

# Example usage:
if __name__ == '__main__':
    n = int(input().strip())
    grades = []
    for _ in range(n):
        grades.append(int(input().strip()))
    result = gradingStudents(grades)
    for grade in result:
        print(grade)
