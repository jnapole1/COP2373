''' This code will sell tickets to the user,while there is still 20 tickets in the system
to sell. The user cannnot buy more than 4 tickes.'''

def main():
    sell_tickets()

#function to have the tickets sold 
def sell_tickets():
    total_tickets = 20  # Total number of tickets available for sale
    total_buyers = 0    # Accumulator to keep track of the total number of buyers

    while total_tickets > 0:  # Loop until all tickets are sold
        print(f"Tickets remaining: {total_tickets}")  # Display the number of remaining tickets

        # Prompt the user to enter the number of tickets they want to buy
        try:
            tickets_requested = int(input("How many tickets would you like to buy (up to 4)? "))

            # Check if the requested number of tickets is valid
            if 1 <= tickets_requested <= 4:
                if tickets_requested <= total_tickets:  # Check if enough tickets are available
                    total_tickets -= tickets_requested  # Deduct the requested tickets from the total
                    total_buyers += 1  # Increment the buyer count
                    print(f"{tickets_requested} tickets purchased. {total_tickets} tickets remaining.\n")
                else:
                    print("Not enough tickets available for that request. Please try again.\n")
            else:
                print("Invalid number of tickets. Please enter a number between 1 and 4.\n")
        
        except ValueError:
            print("Invalid input. Please enter a valid number.\n")
    
    # Display the total number of buyers once all tickets are sold
    print(f"All tickets are sold out. Total number of buyers: {total_buyers}")

# Call the function to start selling tickets
main()
