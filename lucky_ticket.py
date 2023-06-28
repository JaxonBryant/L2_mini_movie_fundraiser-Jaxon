import random

def choose_lucky_ticket(list):
  if len(list) == 0:
    return "No one"
  elif len(list) == 1:
    return list[0]
  else:
    return random.choice(list)