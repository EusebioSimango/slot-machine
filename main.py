import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbolCount = {
  "A": 2,
  "B": 4,
  "C": 6,
  "D": 8
}

def getSlotMAchineSpin(rows, cols, symbols):
  allSymbols = []
  for symbol, symbolCount in symbol.items():
    for _ in range(symbolCount):
      allSymbols.append(symbol)



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

def getBet():
  while True:
    amount  = input(f"What would you like to bet on each line? $")
    if amount.isdigit():
      amount = int(amount)
      if MIN_BET <= amount <= MAX_BET:
        break
      else:
        print(f"Amount must be between ${MIN_BET} and ${MAX_BET}")
    else:
      print("Please enter a number")
  return amount

def main():
  balance = deposit()
  lines = getNumberOfLines()
  while True:
    bet = getBet()
    totalBet = bet * lines

    if totalBet > balance:
      print(f"You do not have enough to bet that amount, your current balance is: {balance} ")
    else:
      break

  print(f"You are betting ${bet} on {lines} lines. Total bet is equal to ${totalBet}.")

main()