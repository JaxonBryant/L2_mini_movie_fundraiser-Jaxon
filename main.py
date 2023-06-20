import string_checker

from get_age import get_ticket_price
from yes_no import yes_no

#Most of this code will be deleted because of ticket_loop and other functions
total_price = 0.0
while True:
  ticket_price = get_ticket_price()
  purchase_confirmation = yes_no("Would you like to buy this ticket? (yes/no): ")
  if purchase_confirmation == True:
    total_price += ticket_price
  purchase_confirmation = False
  exit_ticketpurchase = yes_no("Would you like to purchase another ticket? (yes/no): ")
  if exit_ticketpurchase == True:
    continue
  else:
    print("This will cost ${}".format(total_price))
    break
  


print("Total cost is ${}".format(total_price))