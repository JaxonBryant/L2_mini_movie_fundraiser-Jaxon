def yes_no(question):

  response = input(question).lower().strip()
  if response == "yes" or response == "y":
    print("Program continues ")
    return response
  elif response == "no" or response == "n":
    print("Program continues ")
    return response
  else:
    print("Please input yes or no ")

  #loop for testing
valid = False
while not valid:
  show_instructions = yes_no("Have you purchased tickets for this event before? ")