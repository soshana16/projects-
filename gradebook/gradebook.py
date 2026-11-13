import csv

grades = {}
filepath="/Users/soshana/Desktop/Data-sciencefolder/repo-test/test/projects-/gradebook/grades.csv"
#loads grades
def load_grades():
    global grades
    try:
        with open(filepath, "r") as file:
            reader = csv.reader(file)

            for row in reader:
                if len(row) > 0:
                    subject = row[0].strip().title()
                    grades[subject] = [
                        float(grade) for grade in row[1:]
                    ]
        print("Grades loaded!")
    except FileNotFoundError:
        print("No CSV file found")
    except ValueError:
        print("Invalid CSV data")
        grades = {"Math": [90,75,82], "Science": [89,97,96], "English": [95,93,87]}
#save gradesS
def save_grades():
    try:
        with open('grades.csv', "w", newline="") as file:
            writer = csv.writer(file)

            for subject in grades:
                writer.writerow([subject] + grades[subject])

        print("Grades saved successfully!")
    except FileNotFoundError:
        print("No CSV file found")


#takes subject and grade and adds grade to list
def add_grade(subject, grade):
    subject = subject.strip().title()

    if grade < 0 or grade > 100:
        print("Invalid grade. Enter a number from 0 to 100.")
        return

    if subject not in grades:
        grades[subject] = []

    grades[subject].append(grade)
    print("Grade added successfully!")


#takes subject and prints average
def print_average(subject):
    if subject in grades and len(grades[subject]) > 0:
        average = sum(grades[subject])/len(grades[subject])
        print(subject, "average:", average)
    else:
        print("Subject does not exist or has no grades.")

def print_grades(subject):
    subject = subject.strip().title()

    if subject in grades:
        print(subject, "grades:")
        for grade in grades[subject]:
            print(grade)
    else:
        print("Subject does not exist.")

#prints subject and corresponding average
def print_all_averages():
    averages = {}

    for subject in grades:
        if len(grades[subject]) > 0:
            averages[subject] = sum(grades[subject]) / len(grades[subject])
            print(subject, "average:", averages[subject])

    if averages:
        print("Best subject:", max(averages, key=averages.get))
        print("Worst subject:", min(averages, key=averages.get))
    else:
        print("No grades available.")

#returns users GPA
def get_GPA():
    all_grades = []

    for subject in grades:
        for grade in grades[subject]:
            all_grades.append(grade)

    if not all_grades:
        return 0.0

    average = sum(all_grades) / len(all_grades)

    if average >= 92.5:
        return 4.0
    elif average >= 89.5:
        return 3.7
    elif average >= 79:
        return 3.0
    elif average >= 70:
        return 2.0
    elif average >= 65:
        return 1.0
    else:
        return 0.0
 #removes grade   
def remove_grade(subject, grade):
    subject = subject.strip().title()

    if subject not in grades:
        print("Subject does not exist.")
    elif grade in grades[subject]:
        grades[subject].remove(grade)
        print("Grade removed successfully!")
    else:
        print("Grade not found in this subject.")
#create a visual representation of the user’s average grades across all subjects
def visualize_grades():
    print("\nGrade Visualization")
    print("X = 50%, * = 5%")

    if not grades:
        print("No subjects available.")
        return

    for subject in grades:
        if len(grades[subject]) > 0:
            average = sum(grades[subject]) / len(grades[subject])

            # Round down to nearest 5%
            rounded = int(average // 5) * 5

            # X represents first 50%
            bar = ""
            if rounded >= 50:
                bar = "X"
                bar += "*" * ((rounded - 50) // 5)
            else:
                bar = "*" * (rounded // 5)

            # Align bars
            print(f"{subject:<12}: {bar}")


#menu where functions are tested   
def main():

    load_grades() 

    run_menu = True

    while run_menu:
        print("\n Gradebook Menu")
        print("Current subjects:", ", ".join(grades.keys()))

        print("1. print all class averages")
        print("2. print average for one classS")
        print("3. print overall GPA")
        print("4. add a grade")
        print("5. print grades for a class")
        print("6. remove a grade") 
        print("7. visualize grades")
        print("8. Exit")

        option = input("Choose an option: ")

        if option == "1":
            print_all_averages()
        elif option == "2":
            subject = input("Enter the subject name: ")
            print_average(subject)
        elif option == "3":
            print("Overall GPA:", get_GPA())
        elif option == "4":
            subject = input("Enter the subject name: ")
            grade = float(input("Enter the grade: "))
            add_grade(subject, grade)
            print("A grade was added to the gradebook!")
        elif option == "5":
             subject = input("Enter the subject name: ")
             print_grades(subject)

        elif option == "6":
            subject = input("Enter the subject name: ")
            try:
                grade = float(input("Enter grade to remove: "))
                remove_grade(subject, grade)
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif option == "7":
            visualize_grades()
        elif option == "8":
            save_grades()
            print("Bye!")
            run_menu = False
        else:
            print("Invalid option. Please pick a different option.")

if __name__ == "__main__":
    main()

