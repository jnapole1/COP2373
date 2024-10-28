'''This program allows users to input multiple sentences, including
those that start with numbers. It stores these sentences
and displays each one in the order they were entered,
 with a count of the total number of sentences.
This program is helpful for organizing and counting a
series of inputs and can serve as a simple text collector.'''

# Define a function to take multiple sentences as input
def sentence_input():
    sentences = []  # Initialize an empty list to store sentences
    print("Enter your sentences. Type 'STOP' to end input.")  # Instruction for user

    # Loop to allow continuous input until 'STOP' is entered
    while True:
        sentence = input("Enter a sentence: ")  # Take a sentence as input
        if sentence.upper() == 'STOP':  # Check if the input is 'STOP' (to stop input)
            break  # Exit the loop if 'STOP' is entered
        sentences.append(sentence)  # Add the sentence to the list

    return sentences  # Return the list of sentences


# Function to display sentences and their count
def display_sentences(sentences):
    # Display each sentence
    print("\n--- Sentences Entered ---")
    for i, sentence in enumerate(sentences, 1):  # Enumerate for numbering
        print(f"Sentence {i}: {sentence}")  # Display each sentence with its position number

    # Display the total count of sentences
    print("\nTotal number of sentences:", len(sentences))  # Display the count


# Main function to run the program
def main():
    sentences = sentence_input()  # Call function to get sentences from the user
    display_sentences(sentences)  # Call function to display sentences and count


# Run the main function
 main()
