# Inferior version. Better version on Main.py 
from string_checker import string_check

response = ""
syntax = "a"
tickets_remain = ticket_max
tickets_purchased = 0
yes_no = ["yes", "no"]


while True:
  print("There are {} tickets remaining".format(tickets_remain))
  if tickets_remain <= 0:
    print("No more tickets are available for purchase ")
    return tickets_purchased
  else:
    response = string_check("Would you like to purchase {} ticket? ", 2, yes_no.format(syntax))
    syntax = "another"
    if response == True:
      print("You said yes")
      tickets_remain -= 1
      tickets_purchased += 1
      #llllllllllllllllllllllllllllllllllllllllllllllllllll
      #Note: Connect to calc_ticket_cost here
    elif response == False:
      print("You said no")
      break
    else:
      print("Error")
      continue
  print("You currently have {} tickets ".format(tickets_purchased))

print("You have bought {} ticket(s) ".format(tickets_purchased))