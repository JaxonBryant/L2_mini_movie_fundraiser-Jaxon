def check_input(question):
  while True:
    name = input(question).strip().capitalize()
    if name == "":
      print("Input is blank")
      continue
      
    if name.isdigit():
      print("Input cannot contain digits")
      continue
    else:
      return name


while True:
  name = check_input("What is your name? ")
  print("Name = {}".format(name))
