"""Contains the script for the check_input() function."""
import re


def check_input(question):
  """Return valid input."""
  while True:
    # formatting
    word = input(question).strip().lower().capitalize()
    # check for blank
    if word == "":
      print("Input is blank")
      continue
    # check for digits (! accepted because )
    if re.match(r'^[a-zA-Zāēīōū\s]+$', word):
      return word
    else:
      print("Input cannot contain digits")
      continue
