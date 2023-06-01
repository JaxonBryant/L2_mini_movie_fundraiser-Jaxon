
def yes_no(question, answer_variable):
  while True:
    user_input = input(question).lower().strip()
    if user_input == "yes" or user_input == "y":
      answer_variable = True
      print("You entered yes ")
      break
    elif user_input == "no" or user_input == "n":
      answer_variable = False
      print("You entered no ")
      break
    else:
      print("Invalid input. Please enter 'yes' or 'no'. ")
      return answer_variable

#setting up variables
used_program = False

#Loop for testing
valid = False
while not valid:
  result = yes_no("Have you used this program before? ", used_program)