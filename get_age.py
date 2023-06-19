def get_ticket_price():
  try:
    age = int(input("What is your age? "))
    if age <= 11:
      print("You must be 12+ or you are not able to purchase a ticket.")
    elif age >= 121:
      print("Please input a valid age")
    else:
      if age >= 12 and age <= 16:
          print("You are a teenager: $7.50")
          price = 7.50
      elif age >= 17 and age <= 64:
          print("You are an adult: $10.50")
          price = 10.50
      elif age >= 65 and age <= 120:
          print("You are a senior: $6.50")
          price = 6.50
      else:
        print("Unable to determine ticket price.")
        price = 0.0
        return price
  except:
      print("Input must be an integer (i.e., a number without a decimal part)")
