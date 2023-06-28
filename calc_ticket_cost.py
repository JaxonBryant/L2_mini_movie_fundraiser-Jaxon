#Interchangable ticket cost variables
under_16_ticket = 7.50
adult_ticket = 10.50
senior_ticket = 6.50

# calculate ticket price base on age no feedback 
def calc_ticket_price(age):
  if age >= 12 and age <= 16:
    price = under_16_ticket
  elif age >= 17 and age <= 64:
    price = adult_ticket
  else:
    price = senior_ticket
  return price
