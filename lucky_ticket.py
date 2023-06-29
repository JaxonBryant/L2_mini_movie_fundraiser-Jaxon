import random

#randomly select one name from the list
def choose_lucky_ticket(list):
  if len(list) == 0:
    #in case the program is finished before any names are input
    return "No one"
  elif len(list) == 1:
    return list[0]
  else:
    return random.choice(list)