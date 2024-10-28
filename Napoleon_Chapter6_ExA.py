''' this program will ask the user for their soical,phone number, and zip code
and the code will let the user know if it matches the program or not '''

#importing re to allow regular expressions
import re


# Function to validate phone numbers (Format: (XXX) XXX-XXXX or XXX-XXX-XXXX)
def validate_phone_number(phone_number):
    # Regular expression to match phone numbers
    phone_regex = re.compile(r'^(\(\d{3}\)\s|\d{3}-)\d{3}-\d{4}$')
    if phone_regex.match(phone_number):
        return True
    return False


# Function to validate Social Security numbers (Format: XXX-XX-XXXX)
def validate_ssn(ssn):
    # Regular expression to match SSNs
    ssn_regex = re.compile(r'^\d{3}-\d{2}-\d{4}$')
    if ssn_regex.match(ssn):
        return True
    return False


# Function to validate ZIP codes (Format: 5 digits or 5 digits-4 digits)
def validate_zip_code(zip_code):
    # Regular expression to match ZIP codes
    zip_code_regex = re.compile(r'^\d{5}(-\d{4})?$')
    if zip_code_regex.match(zip_code):
        return True
    return False


# Main function to get input from user and validate the inputs
def main():
    print("Please enter the following details for validation:")

    # Get user input
    phone_number = input("Enter a phone number (format: XXX-XXX-XXXX or (XXX) XXX-XXXX): ")
    ssn = input("Enter a Social Security Number (format: XXX-XX-XXXX): ")
    zip_code = input("Enter a ZIP code (format: XXXXX or XXXXX-XXXX): ")

    # Validate phone number
    if validate_phone_number(phone_number):
        print(f"Phone number '{phone_number}' is valid.")
    else:
        print(f"Phone number '{phone_number}' is invalid.")

    # Validate SSN
    if validate_ssn(ssn):
        print(f"Social Security Number '{ssn}' is valid.")
    else:
        print(f"Social Security Number '{ssn}' is invalid.")

    # Validate ZIP code
    if validate_zip_code(zip_code):
        print(f"ZIP code '{zip_code}' is valid.")
    else:
        print(f"ZIP code '{zip_code}' is invalid.")


# Test the functions with various inputs
if __name__ == "__main__":
    # Example of test cases
    print("\nRunning test cases...\n")

    # Test valid phone numbers
    print("Testing phone numbers:")
    print(validate_phone_number("123-456-7890"))  # True
    print(validate_phone_number("(123) 456-7890"))  # True
    print(validate_phone_number("1234567890"))  # False
    print()

    # Test valid SSNs
    print("Testing SSNs:")
    print(validate_ssn("123-45-6789"))  # True
    print(validate_ssn("123-456-789"))  # False
    print()

    # Test valid ZIP codes
    print("Testing ZIP codes:")
    print(validate_zip_code("12345"))  # True
    print(validate_zip_code("12345-6789"))  # True
    print(validate_zip_code("1234"))  # False
    print()

    # Run the main function to allow user input
    main()
