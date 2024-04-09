import getpass

# This function will check the user's input for numbers, uppercase and lowercase
# characters, and symbols. It will return a boolean value for each.
def check_string_components(s):
    # Check for numeric characters
    has_numeric = any(char.isnumeric() for char in s)
    # Check for uppercase letters
    has_upper = any(char.isupper() for char in s)
    # Check for lowercase letters
    has_lower = any(char.islower() for char in s)
    # Check for symbols (considering anything that isn't alphanumeric as a symbol)
    has_symbols = any(not char.isalnum() for char in s)

    return has_numeric, has_upper, has_lower, has_symbols

# We will use this function to get a password from the user.
def get_password():
    # Here I use the getpass module to mask the user's input.
    return getpass.getpass("Please enter a password: ")

# Call the function
password = get_password()

# Check the string for each requirement
numeric, upper, lower, symbols = check_string_components(password)

# Check if the values return true
values_check = (numeric, upper, lower, symbols)
all_values = all(values_check)
if all_values == True and len(password) >= 8:
    print("This is a great password!")
else:
    print("A strong password inclues numbers, symbols, uppercase and lowercase letters, and is 8 or more characters long.")