from string_checker import string_check
from calc_ticket_cost import calc_ticket_price
from get_age import get_age
from blank_input import check_input
from lucky_ticket import choose_lucky_ticket

#ticket costs can be changed in the calc_ticket_price function, bt in the future it will be able to be here if all functions are moved here.

#Setting up variables
response = ""
syntax = "a"
ticket_max = 5
tickets_remain = ticket_max
tickets_purchased = 0
yes_no = ["yes", "no"]
choose_payment_method = ["cash", "credit"]
ticket_loop = True
lucky_ticket = []

while ticket_loop == True:
  print("------------------------------------------------------------") #to visually seperate purchases
  print("There are {} tickets remaining".format(tickets_remain))
  if tickets_remain <= 0:
    print("No more tickets are available for purchase ")
    ticket_loop = False
  else:
    response = string_check("Would you like to purchase {} ticket? ".format(syntax), 2, yes_no)
    syntax = "another"
    if response == 'yes':
      print("You said yes")
      tickets_remain -= 1
      tickets_purchased += 1
      name = check_input("What is your name: ")
      lucky_ticket.append(name)
      print(lucky_ticket)
      #age = get_age()
      #print(age)
      #price = calc_ticket_price(age)
      #print(price)
      #payment_method = string_check("Cash or credit: ", 2, choose_payment_method)
      #if payment_method == "cash":
        #print("Cash")
      #else:
        #print("Credit")
      #Confirm purchase function
    else:
      print("You said no")
      break
  #print("Name: {}, Age: {}, Cost: ${:.2f}, Payment: {}".format(name, age, price, payment_method))
  print("{} ticket(s) have been sold".format(tickets_purchased))

print("------------------------------------------------------------")
print("You have bought {} ticket(s) ".format(tickets_purchased))
lucky_ticket_holder = choose_lucky_ticket(lucky_ticket)
print("{} has the lucky ticket".format(lucky_ticket_holder))