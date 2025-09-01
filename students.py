# List of student dictionaires
students = [
    {"name": "Alice", "age": 21, "grade": 85},
    {"name": "Bob", "age": 22, "grade": 78},
    {"name": "Charlie", "age": 20, "grade": 92},
    {"name": "Umu", "age": 28, "grade": 88},
    {"name": "Hawa", "age": 29, "grade": 74}
]

# Function to calculate average grade
def calculate_average_grade(students):
    total_grade = 0
    for student in students:
        total_grade += student["grade"]  
    average = total_grade / len(students)
    return average

# Function to find students with grade above 80
def find_passing_students(students):
    passing_students = []
    for student in students:
        if student["grade"] > 80: 
            passing_students.append(student)
    return passing_students 

# Function to sort students by grade in descending order
def sort_students_by_grade(students):
    students.sort(key=lambda student: student["grade"], reverse=True)
    return students

# Function to print student details
def print_students(students):
    for student in students:
        print(f"Student: {student['name']}, Grade: {student['grade']}")

# Main program flow
print("All Students:")
print_students(students)

avg_grade = calculate_average_grade(students)
print(f"\nAverage Grade: {avg_grade:.2f}")

passing = find_passing_students(students)
print("\nPassing Students (grade > 80):")
print_students(passing)

sorted_students = sort_students_by_grade(students)
print("\nStudents Sorted by Grade (Descending):")
print_students(sorted_students)
