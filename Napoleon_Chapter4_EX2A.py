''' this function will ask the user how much they spend on expenses
and then return their total exense, while also returning the
highest and lowest expense'''

from functools import reduce

# Function to get monthly expenses from the user
def get_expenses():
    expenses = []
    while True:
        # Ask for the type of expense and amount
        expense_type = input("Enter the type of expense (or 'done' to finish): ")
        if expense_type.lower() == 'done':
            break
        try:
            amount = float(input(f"Enter the amount for {expense_type}: "))
            expenses.append((expense_type, amount))  # Store as a tuple of (type, amount)
        except ValueError:
            print("Invalid amount. Please enter a numeric value.")
    return expenses

# Main function to process expenses
def analyze_expenses(expenses):
    # Calculate the total using reduce with a lambda function
    total_expense = reduce(lambda x, y: x + y[1], expenses, 0)

    # Find the highest expense using reduce
    highest_expense = reduce(lambda x, y: x if x[1] > y[1] else y, expenses)

    # Find the lowest expense using reduce
    lowest_expense = reduce(lambda x, y: x if x[1] < y[1] else y, expenses)

    # Display the results
    print(f"\nTotal expense: ${total_expense}")
    print(f"Highest expense: {highest_expense[0]} - ${highest_expense[1]}")
    print(f"Lowest expense: {lowest_expense[0]} - ${lowest_expense[1]}")

# Main program execution
def main():
    # Get the list of expenses from the user
    expenses = get_expenses()

    # If there are expenses, analyze them
    if expenses:
        analyze_expenses(expenses)
    else:
        print("No expenses entered.")

main()