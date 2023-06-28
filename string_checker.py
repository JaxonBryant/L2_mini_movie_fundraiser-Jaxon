def string_check(question, num_letter, valid_list):
  error = "Please choose {} or {} ".format(valid_list[0],valid_list[1])
    
  while True:
    response = input(question).lower().strip()
    for item in valid_list:
      if response == item[:num_letter] or response in item:
        return item
    print(error)