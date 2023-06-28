#Replaced by string_checker. No longer used.
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