'''
This program allows an instructor to store students' exam scores and display them.
The first part of the program collects each student's details and writes this
 information to a CSV file named grades.csv.
'''

import csv

# Function to read and display the grades from the CSV file
def display_grades_from_csv():
    # File name
    filename = 'grades.csv'

    # Open the file in read mode
    with open(filename, mode='r') as file:
        # Create a CSV reader object
        reader = csv.reader(file)

        # Read the header
        header = next(reader)

        # Print the header
        print(f"{header[0]:<15} {header[1]:<15} {header[2]:<10} {header[3]:<10} {header[4]:<10}")
        print("-" * 60)

        # Read and display each student's record
        for row in reader:
            print(f"{row[0]:<15} {row[1]:<15} {row[2]:<10} {row[3]:<10} {row[4]:<10}")




def write_grades_to_csv():
    # File name
    filename = 'grades.csv'

    # Get the number of students to enter
    num_students = int(input("Enter the number of students: "))

    # Open the file in write mode
    with open(filename, mode='w', newline='') as file:
        # Create a CSV writer object
        writer = csv.writer(file)

        # Write the header to the CSV file
        writer.writerow(["First Name", "Last Name", "Exam 1", "Exam 2", "Exam 3"])

        # Loop to get each student's details
        for _ in range(num_students):
            # Get student's first and last names
            first_name = input("Enter student's first name: ")
            last_name = input("Enter student's last name: ")

            # Get student's exam grades
            exam1 = int(input("Enter Exam 1 grade: "))
            exam2 = int(input("Enter Exam 2 grade: "))
            exam3 = int(input("Enter Exam 3 grade: "))

            # Write the student's record as a row in the CSV file
            writer.writerow([first_name, last_name, exam1, exam2, exam3])

    print(f"Data saved to {filename} successfully.")


# Call the function to start the progra

def main():
    write_grades_to_csv()
    display_grades_from_csv()

main()