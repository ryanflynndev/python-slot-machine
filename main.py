import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

SYMBOLS = {
  "A": 2,
  "B": 4,
  "C": 6,
  "D": 8,
}

SYMBOL_VALUES = {
  "A": 8,
  "B": 6,
  "C": 4,
  "D": 2,
}

def check_winnings(columns, lines, bet, values):
  winnings = 0
  for line in range(lines):
    symbol = columns[0][line]
    for col in columns:
      symbol_to_check = col[line]
      if symbol != symbol_to_check:
        break
    else:
      winnings += values[symbol] * bet

  return winnings


def get_slot_machine_spin(rows, cols, symbols):
  all_symbols = []
  for symbol, symbol_count in symbols.items():
    for _ in range(symbol_count):
      all_symbols.append(symbol)

  columns = []
  for _ in range(cols):
    column = []
    current_symbols = all_symbols[:]
    for _ in range(rows):
      value = random.choice(current_symbols)
      current_symbols.remove(value)
      column.append(value)

    columns.append(column)

  return columns

def deposit():
  while True:
    prompt = "What would you like to deposit? $"
    amount = input(prompt)
    if amount.isdigit():
      amount = int(amount)
      if amount > 0:
        break
      else: 
        print("Amount must be greater than 0.")
    else:
      print("Please enter a number.")

  return amount

def get_num_of_lines():
  while True:
    prompt = "Enter number of lines to bet on (1-" + str(MAX_LINES) + ")? "
    lines = input(prompt)
    if lines.isdigit():
      lines = int(lines)
      if 1 <= lines <= MAX_LINES:
        break
      else: 
        print("Enter a valid number of lines")
    else:
      print("Please enter a number.")

  return lines

def get_bet(): 
  while True:
    prompt = "What would you like to bet on each line? $"
    bet = input(prompt)
    if bet.isdigit():
      bet = int(bet)
      if MIN_BET <= bet <= MAX_BET:
        break
      else: 
        print(f"Amount must be between {MIN_BET} - {MAX_BET}")
    else:
      print("Please enter a number.")

  return bet

def print_slot_machine(columns):
  # transposing matrix
  for row in range(len(columns[0])):
    for i, column in enumerate(columns):
      if i != len(columns) - 1:
        print(column[row], end=" | ")
      else:
        print(column[row], end="")

    print()

def main():
  balance = deposit()
  lines = get_num_of_lines()
  while True:
    bet = get_bet()
    total_bet = bet * lines
    max_bet = round(balance / lines, 2)
    if total_bet >= balance:
      print(f"You do not have enough to bet that amount, your current balance is: ${balance}. The max bet you can do is ${max_bet}")
    else:
      break
  print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")


  slots = get_slot_machine_spin(ROWS, COLS, SYMBOLS)
  print_slot_machine(slots)


main()
