#import functions
from string_checker import string_check
from calc_ticket_cost import calc_ticket_price
from get_age import get_age
from blank_input import check_input
from lucky_ticket import choose_lucky_ticket

#ticket costs can be changed in the calc_ticket_price function, but it could be moved here if all functions are moved here too.

#inputting the "password" into the name bracket will end the ticket loop and begin the end process.

#Set up variables
response = ""
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
PASSWORD = "Break xxx" #Must start with capital
#profit calculation is the difference between the price of tickets and the profit per ticket.
profit_calculation = price - 5

while ticket_loop == True:
  print("------------------------------------------------------------") #to visually seperate purchases
  print("There are {} tickets remaining".format(tickets_remain))
  if tickets_remain <= 0:
    print("No more tickets are available for purchase ")
    ticket_loop = False
  else:
    response = string_check("Would you like instructions to help guide you as you use the program? Enter yes or no: ", 2, yes_no)
    if response == 'yes':
      #This is a list containing addons to sentences later. The list is in the program beause it can be changed but needs to be able to be reset. It is messy but works
      instructions = ["(Type in the full name of whoever this ticket is for (you or whoever you are buying this ticket for). This name will be called out if your ticket wins you the lucky prize, so make sure it is real and recognizable) \n", "(Type in the age of the user. The age will determine the price of the ticket. Remember to input the real age of whoever this ticket is for)\n", "(Type in 'Cash' or 'Credit' to say how you will be paying for this ticket)\n"]
      print("You said yes")
    else:
      #removes instruction text from loop
      instructions = ["", "", "", ""]
      print("You said no")
    #get data of user
    name = check_input("{}Name: ".format(instructions[0]))
    if name == PASSWORD:
      ticket_loop = False
      break
    else:
      lucky_ticket.append(name)
      print(lucky_ticket)
      print("Ages 12-16 = $7.50 \nAges 17-64 = $10.50 \nAges 65- = $6.50")
      age = get_age("{}Age: ".format(instructions[1]))
      print(age)
      #calc ticket cost and profit
      price = calc_ticket_price(age)
      print(price)
      money_spent = money_spent + price
      solo_profit = price + profit_calculation
      profit = profit + solo_profit
      payment_method = string_check("{}Cash or credit: ".format(instructions[2]), 2, choose_payment_method)
      tickets_remain -= 1
      tickets_purchased += 1
  #find payment method
  if payment_method == "cash":
    print("Cash")
  else:
    print("Credit")
  #print data of user for confirmation
  print("Name: {}, Age: {}, Cost: ${:.2f}, Payment: {}".format(name, age, price, payment_method))
  #print("{} ticket(s) have been sold".format(tickets_purchased))

print("------------------------------------------------------------")
print("{} ticket(s) have been sold ".format(tickets_purchased))
#randomly pick one name which has bought a ticket
lucky_ticket_holder = choose_lucky_ticket(lucky_ticket)
print("{} won the lucky ticket".format(lucky_ticket_holder))
print("${} was spent on tickets, ${} was earnt as profit ".format(money_spent, profit))

#Changed a few minor things like "constant variable" capitalization, front user readability