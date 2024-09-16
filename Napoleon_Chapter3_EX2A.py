''' this program will comb through the users email to
detect any phrases in the list bellow. If dtetcted the prgoram
will let the user know the spam likely score and spam score'''

# List of common spam words and phrases
spam_keywords = [
    'promo', 'claim', 'cash', 'trial', 'unlimited', 'cheap', 'earn money', 'win', 'winner',
    'act now', 'gift', 'offer', 'order now', 'congratulations', 'credit card', 'risk-free',
    'as seen on', 'buy now', 'limited time', 'urgent', 'exclusive', 'prize', 'click here',
    'discount', 'no cost', 'investment', 'free', 'guarantee', 'bonus', '100% free'
]


# Function to calculate the spam score based on keywords found in the email
def calc_spam_score(email_message):
    # Initialize spam score
    spam_score = 0
    # Initialize a list to keep track of keywords found
    keywords_found = []

    # case insensitive search
    email_message = email_message.lower()

    # Loop through each spam keyworr
    for keyword in spam_keywords:
        if keyword in email_message:
            spam_score += 1  # Increment spam score for each occurrence
            keywords_found.append(keyword)  # Add the keyword to the list of found keywords

    return spam_score, keywords_found

# Function to rate the likelihood of the email being spam based on spam score
def rate_spam_likelihood(spam_score):
    if spam_score == 0:
        return "The email is not spam."
    elif spam_score <= 5:
        return "The email is unlikely to be spam."
    elif spam_score <= 10:
        return "The email might be spam."
    elif spam_score <= 20:
        return "The email is likely spam."
    else:
        return "The email is almost certainly spam."

# Main function to get user input and display spam score and likelihood
def main():
    # Pask ser for email
    email_message = input("Enter the email message to check for spam: ")

    # calc spam score
    spam_score, keywords_found = calc_spam_score(email_message)

    # how spam likly
    spam_likelihood = rate_spam_likelihood(spam_score)

    # Display the spam score and spam likelihood
    print(f"\nSpam Score: {spam_score}")
    print(f"Spam Likelihood: {spam_likelihood}")

    # Display the keywords of  spam
    if keywords_found:
        print("The following spam keywords were found in the message:")
        for keyword in keywords_found:
            print(f"- {keyword}")
    else:
        print("No spam keywords were found in the message.")

# Run the main function
main()
