#import functions
from string_checker import string_check
from calc_ticket_cost import calc_ticket_price
from get_age import get_age
from blank_input import check_input
from lucky_ticket import choose_lucky_ticket

#ticket costs can be changed in the calc_ticket_price function, but it could be moved here if all functions are moved here too.

#Set up variables
response = ""
syntax = "a"
ticket_max = 5
tickets_remain = ticket_max
tickets_purchased = 0
yes_no = ["yes", "no"]
choose_payment_method = ["cash", "credit"]
ticket_loop = True
lucky_ticket = []
money_spent = 0
profit = 0
price = 0
#profit calculation is the difference between the price of tickets and the profit per ticket.
profit_calculation = price - 5

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
      #get data of user
      name = check_input("What is your name: ")
      lucky_ticket.append(name)
      print(lucky_ticket)
      age = get_age()
      print(age)
      #calc ticket cost and profit
      price = calc_ticket_price(age)
      print(price)
      money_spent = money_spent + price
      solo_profit = price + profit_calculation
      profit = profit + solo_profit
      payment_method = string_check("Cash or credit: ", 2, choose_payment_method)
      #find payment method
      if payment_method == "cash":
        print("Cash")
      else:
        print("Credit")
      #Confirm purchase
    else:
      print("You said no")
      break
  print data of user for confirmation
  print("Name: {}, Age: {}, Cost: ${:.2f}, Payment: {}".format(name, age, price, payment_method))
  print("{} ticket(s) have been sold".format(tickets_purchased))

print("------------------------------------------------------------")
print("{} ticket(s) have been bought ".format(tickets_purchased))
#randomly pick one name which has bought a ticket
lucky_ticket_holder = choose_lucky_ticket(lucky_ticket)
print("{} has the lucky ticket".format(lucky_ticket_holder))
print("${} was spent on tickets, ${} was earnt as profit ".format(money_spent, profit))