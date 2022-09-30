MAX_LINES = 3



def deposit():
  while True:
    amount  = input("What would you like to deposit? $")
    if amount.isdigit():
      amount = int(amount)
      if amount > 0:
        break
      else:
        print("The amount must be grater than 0.")
    else:
      print("Please enter a number")
  return amount

def getNumberOfLines():
  while True:
    lines  = input(f"Enter the number of lines to bet on (1-{MAX_LINES})? ")
    if lines.isdigit():
      lines = int(lines)
      if 1 <= lines <= MAX_LINES:
        break
      else:
        print("Enter a valid number of lines")
    else:
      print("Please enter a number")
  return lines



def main():
  balance = deposit()
  lines = getNumberOfLines()
main()