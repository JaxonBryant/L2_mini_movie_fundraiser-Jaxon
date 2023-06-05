def yes_no(question):
    detect_truefalse = None  # Initialize the variable
    while detect_truefalse is None:
        user_input = input(question).lower().strip()
        if user_input == "yes" or user_input == "y":
            detect_truefalse = True
        elif user_input == "no" or user_input == "n":
            detect_truefalse = False
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
    return detect_truefalse  # Return the value at the end of the function

# Setting up variables
used_program = False

# Loop for testing
valid = False
while not valid:
    result = yes_no("Have you used this program before? ")
    if result == True:
        print("You said yes")
        continue
    elif result == False:
        print("You said no")
        continue
    else:
        print("Error")
        continue