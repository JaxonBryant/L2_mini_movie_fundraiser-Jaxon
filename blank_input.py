import re

def check_input(question):
  while True:
    #formatting
    word = input(question).strip().lower().capitalize()
    #check for blank
    if word == "":
      print("Input is blank")
      continue
    #check for digits (! accepted because )
    if re.match(r'^[a-zA-Zāēīōū\s]+$', word):
      return word
    else:
      print("Input cannot contain digits")
      continue