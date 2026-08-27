def show_menu():    #   Made this a funtion to call it every time a loop repeats
    print("\n===== Bright Future High School - Student Records =====")
    print("1. Add Students(s)")
    print("2. View All Students")
    print("3. Calculate and View Averages")
    print("0. Exit")
    print("=========================")

def add_students(students): #   add students
    #   ask how many students to add
    num = int(input("How many students would you like to add? "))

    for i in range(num):
        print(f"\n--- Student {i + 1} ---")
        name = input("Enter student name: ")

        # grade = input("Enter student grade (8 - 12): ")

        while True:
            try:
                grade = int(input("Enter student grade (8 - 12): "))
                if 8 <= grade <= 12:
                    break
                else:
                    print("Grade must be between 8 and 12.")
            except ValueError:
                print("Invalid input! Please enter a whole number.")

        marks = []  #   list for the marks
        for term in range(1, 5):    #   loops for Term 1 to Term 4
            # mark = float(input(f"Enter Term {term} mark: "))

            while True:
                try:
                    mark = float(input(f"Enter Term {term} mark: "))
                    if 0 <= mark <= 100:
                        break
                    else:
                        print("Mark must be between 0 and 100.")
                except ValueError:
                    print("Invalid input! Please enter a number.")

            marks.append(mark)

        #   stores everything as one dict, then adds to the list
        student = {"name": name, "grade": grade, "marks": marks}
        students.append(student)

    print(f"\n{num} student(s) added successfully!")

def view_students(students):    #   display students
    if not students:    #   Checks if list is empty
        print("\nNo students have been added yet.")
        return

    print("\n----- Student Records -----")
    for student in students:
        print(f"Name: {student['name']}")
        print(f"Grade: {student['grade']}")
        print(f"Term Marks: {student['marks']}")
        print("-" * 27)

def view_averages(students):    #   calculate averages
    if not students:
        print("\nNo students have been added yet.")
        return

    print ("\n----- Student Averages -----")
    for student in students:
        total = sum(student["marks"])   #   add up the four marks
        average = total / len(student["marks"]) #   divide by number or terms
        print(f"{student['name']} (Grade {student['grade']}): Average = {average:.2f}%")

def main(): #   main loop
    students = [] # Holds studentn records

    #   What it will look like
    #   {"name": "Bongi", "grade": 10, "marks": [65, 70, 84, 75]}

    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            add_students(students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            view_averages(students)
        elif choice == "0":
            print("Closing the application. Goodbye!")
            break   #   exits while loop, ending program
        else:
            #   Handles invalid menu option
            print("Invalid option. Please choose a number from the menu.")

if __name__ == "__main__":  #   runs the program
    main()