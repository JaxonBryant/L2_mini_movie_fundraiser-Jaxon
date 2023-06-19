from yes_no import yes_no

def ticket_loop(ticket_max):
  response = ""
  syntax = "a"
  tickets_remain = ticket_max
  tickets_purchased = 0
  while True:
    print("There are {} tickets remaining".format(tickets_remain))
    if tickets_remain <= 0:
      print("No more tickets are available for purchase ")
      return tickets_purchased
    else:
      response = yes_no("Would you like to purchase {} ticket? ".format(syntax))
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