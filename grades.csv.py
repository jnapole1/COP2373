import csv


# Function to get student details and write to a CSV file
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


# Call the function to start the program
write_grades_to_csv()
