def string_check(question, num_letter, valid_list):
  error = "Please choose {} or {} ".format(valid_list[0],valid_list[1])
    
  while True:
    response = input(question).lower().strip()
    for item in valid_list:
      #stop "c" automatically equalling cash when it could be both cash or credit
      if response == "c":
        continue
      if response == item[:num_letter] or response in item:
        #allow partial responses EG cred, ye, ash.
        return item
    print(error)