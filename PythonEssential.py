# modify this code and make a input field in which user enter a positive number so it shows the success msg or else through the value eror

def check_positive_number(num):
    if num < 0:
        raise ValueError("The number must be positive!")
    return num

# Example usage
try:
    check_positive_number(-5)
except ValueError as e:
    print(e)




def check_positive_number(num):
    # Check if the number is less than 0
    if num < 0:
        # Raise a ValueError with a custom message
        raise ValueError("The number must be positive!")
    
    # If the number is positive, return it
    return num

# Main program execution
try:
    # Ask the user to input a number and convert it to a float
    user_input = float(input("Enter a positive number: "))
    
    # Call the function to check if the number is positive
    result = check_positive_number(user_input)
    
    # If no exception occurs, print a success message
    print(f"Success! You entered a positive number: {result}")

# Catch any ValueError that is raised
except ValueError as e:
    # Print the error message
    print(e)
