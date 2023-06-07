def get_age():
#loop for testing
  while True:
    try:
      age = int(input("What is your age? "))
      if age <= 11 or age >= 121:
        print("Invalid age, you are not able to purchase a ticket.")
      else:
        if age >= 12 and age <= 16:
          print("You are a teenager: $7.50")
          continue
          
        elif age >= 17 and age <= 64:
          print("You are an adult: $10.50")
          continue
          
        elif age >= 65 and age <= 120:
          print("You are a senior: $6.50")
          continue
          
        else:
          print("error")
          continue
    except:
      print("Input must be a full number")
      continue