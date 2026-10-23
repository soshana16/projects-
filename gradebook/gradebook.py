grades = {"Math": [90,75,82], "Science": [89, 97, 96], "English": [95, 93, 87]}

#takes subject and grade and adds grade to list
def add_grade(subject, grade):
    subject=subject.title()
    if subject not in grades:
        grades[subject] = []
    grades[subject].append(grade)
#takes subject and prints average
def print_average(subject):
    if subject in grades and len(grades[subject]) > 0:
        average = sum(grades[subject])/len(grades[subject])
        print(subject, "average:", average)
    else:
        print("Subject does not exist or has no grades.")

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
#menu where functions are tested   
def main():

    run_menu = True

    while run_menu:
        print("\n Gradebook Menu")
        print("1. print all class averages")
        print("2. print grades for a class")
        print("3. print overall GPA")
        print("4. add a grade")
        print("5. Exit")

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
            print("Bye!")
            run_menu = False
        else:
            print("Invalid option. Please pick a different option.")

if __name__ == "__main__":
    main()

