from get_age import get_age

under16_price = 7.50
adult_price = 10.50
senior_price = 6.50


def calc_ticket_price():
  age = get_age()
  if age is not None:
      if age >= 12 and age <= 16:
        print("Would you like to purchase an under 16 ticket: ${}".format(under16_price))
        price = 7.50
      elif age >= 17 and age <= 64:
        print("Would you like to purchase an adult ticket: ${}".format(adult_price))
        price = 10.50
      elif age >= 65 and age <= 120:
        print("Would you like to purchase an under 16 ticket: ${}".format(senior_price))
      else:
        print("Unable to determine ticket price.")
        price = 0.0  # Set a default price in case the age doesn't match any category
      return price 
  else:
    return None  # Return None if the age is not valid
