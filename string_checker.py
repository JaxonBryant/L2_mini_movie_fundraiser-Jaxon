def string_check(question, num_letter, valid_list):
  error = "Please choose {} or {} ".format(valid_list[0],valid_list[1])
    
  while True:
    response = input(question).lower().strip()
    for item in valid_list:
      if response == item[:num_letter] or response in item:
        return item
    print(error)

payment_method = ["cash", "credit"]
valid = False
while not valid:
  payment_method_input = string_check("Please enter cash or credit ", 2, payment_method)
  print(payment_method_input)
  #find what the input was
  if payment_method_input == payment_method[0]:
    print("You used cash")
  else:
    print("You used credit")