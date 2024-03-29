"""Function for forcing valid input of age."""
# rename the function and remove the print statements


def get_age(question):
  """Return valid integer input."""
  while True:
    # force valid input
    try:
      age = int(input(question).strip())
      if age <= 11:
        print("You must be 12+ to purhase a ticket")
      elif age >= 121:
        print("Please input a valid age")
      elif age == "":
        print("Input blank. Please try again")
      else:
        return age
        break
    except ValueError:
        print("Input must be an integer (i.e., a number without a decimal part)")
