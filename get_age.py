def get_age():
#loop for testing
  while True:
    try:
      age = int(input("What is your age? "))
      if age <= 11: #stop invalid inputs
        print("You must be 12+ or you are not able to purchase a ticket.")
      elif age >= 121:
        print("Please input a valid age")
      else: #find age bracket
        if age >= 12 and age <= 16:
          print("You are a teenager: $7.50")
        elif age >= 17 and age <= 64:
          print("You are an adult: $10.50")
        elif age >= 65 and age <= 120:
          print("You are a senior: $6.50")
        else: #emergency that should never happen
          print("error")
    except: #simple explanation for doing it properly
      print("Input must be an integer (ie: a number which does not have a decimal part) ")
      