def main():
    while True:
        print("STUDENT INFORMATION MANAGEMENT SYSTEM")
        print("1.ADD A NEW STUDENT")
        print("2.VIEW ALL STUDENTS")
        print("3.CHECK IF A STUDENT PASSED OR FAILED")
        print("4.CALCULATE AVERAGE GRADE")
        print("5.VIEW STUDENT NAMES IN UPPERCASE")
        print("6.RANK STUDENTS BY GRADE")
        print("7.EXIT")
        print("8.RATE THE PROGRAM ")
        choice = int(input("CHOOSE AN OPTION (1-8): "))

        if choice == 1:
            add_student()
        elif choice == 2:
            view_students()
        elif choice == 3:
            check_pass_fail()
        elif choice == 4:
            calculate_average_grade()
        elif choice == 5:
            view_names_uppercase()
        elif choice == 6:
            rank_student()
        elif choice == 7:
            confirm_exit()
        elif choice == 8:
            rate_program()
        else:
            print("INVALID CHOICE. PLEASE CHOOSE AN OPTION BETWEEN 1 AND 8.")


students = []


def add_student():
    name = str(input("Enter student's name: "))
    age = int(input("Enter student's age: "))
    grade = float(input("Enter student's grade: "))

    details = {
        "name": name,
        "age": age,
        "grade": grade
    }
    students.append(details)
    print(f"Student {name} added successfully!")


def view_students():
    if not students:
        print("No students available to display.")

        return

    print("\nStudents List:")
    for student in students:
        print(f"Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}")


def check_pass_fail():
    if not students:
        print("No students available.")
        return
    name = input("Please input the name of the student: ")
    student = next((s for s in students if s['name'].lower() == name.lower()), None)

    if student is None:
        print("Student not found.")
    else:
        if student['grade'] >= 50:
            print(f"{student['name']} passed.")
        else:
            print(f"{student['name']} failed.")


def calculate_average_grade():
    if not students:
        print('there are no grades to count')
    average = sum(student['grade'] for student in students) / len(students)
    print(f"Average grade: {average}")


def view_names_uppercase():
    if not students:
        print("No students available to display.")
        return

    print("\nStudent Names in Uppercase:")
    for s in students:
        print(s['name'].upper())


def rank_student():
    if not students:
        print("No students available to rank.")
        return

    students.sort(key=lambda s: s['grade'], reverse=True)
    print("\nRanked Students List:")
    for rank, student in enumerate(students, 1):
        print(f"{rank}. Name: {student['name']}, Grade: {student['grade']}")


def confirm_exit():
    choice = input("Are you sure you want to exit? (yes/no): ").lower()
    if choice == 'yes':
        print("Exiting the program, thank you for using the program.")
    else:
        print("The program will continue running in the background.")


def rate_program():
    print("\nRate our program:")
    print("1. Excellent")
    print("2. Good")
    print("3. Average")
    print("4. Poor")
    print("5. Terrible")

    rate = int(input("Choose a number (1-5): "))
    if 1 <= rate <= 5:
        print("Thanks for your feedback!")
    else:
        print("Invalid rating. Please enter a number between 1 and 5.")


main()