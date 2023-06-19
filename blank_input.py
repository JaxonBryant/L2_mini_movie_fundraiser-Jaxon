def check_input(question):
  while True:
    #formatting
    name = input(question).strip().lower().capitalize()
    #check for blank
    if name == "":
      print("Input is blank")
      continue
    #check for digits
    if name.isdigit():
      print("Input cannot contain digits")
      continue
    else:
      return name


#loop for testing
while True:
  name = check_input("What is your name? ")
  print("Name = {}".format(name))
