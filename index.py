students = {'John', 'Maria', 'David', 'Samantha'}
index = int(input("Enter the index: "))

students_list = list(students)

if 0 <= index < len(students_list):
    print(students_list[index])
else:
    print("Index out of range")