import random

# Defining constants
MAX_LINES=3
MAX_BET = 100
MIN_BET = 1
ROWS=3
COLS=3
# Creating symbols and maximum amount of it which will be shown in the slot machine
symbol_count= {"A":5,
               "B":6,
               "C":7,
               "D":8}
# Value of the symbols. A has higher value because it has lower chance to generate
symbol_value= {"A":5,
               "B":4,
               "C":3,
               "D":2}

# Checking whether we are winning
def check_winings(columns, lines , bet, values):
    winnings= 0
    winning_lines= []
    for line in range(lines):
        symbol= columns[0][line]
        for column in columns:
            symbol_to_check= column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings= winnings+ values[symbol]*bet
            winning_lines.append(line+1)
    return winnings,winning_lines
def get_slot_machine_spin(rows,cols,symbols):
    all_symbols=[]
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column=[]
        current_symbols=all_symbols[:]
        for _ in range(rows):
            value=random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)
    return columns

# transposing
def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i,column in enumerate(columns):
            if i != len(columns) - 1 :
                print(column[row],end=" | ")
            else:
                print(column[row], end=" ")
        print()

# Creating a function which will take the deposit of the player
def deposit():
    while True:
        amount = input("How much would you like to deposit? $")
        if amount.isdigit():
            amount=int(amount)
            if amount > 0:
                break
            else:
                print("Deposit must be greater than $0")
        else:
            print("Please enter a number")
    return amount

# The number of lines that a player will bet on
def get_lines():
    while True:
        lines = input("Enter the number of lines (1- " + str(MAX_LINES) +   ") ")
        if lines.isdigit():
            lines=int(lines)
            if 1<= lines <= MAX_LINES:
                break
            else:
                print("Enter between (1-3)")
        else:
            print("Please enter a number")
    return lines

# Amount of money a player will bet on
def get_bet():
    while True:
        bets = input("How much would you bet on each line? $")
        if bets.isdigit():
            bets = int(bets)
            if MIN_BET <= bets <= MAX_BET:
                break
            else:
                print(f"Enter between ${MIN_BET} - ${MAX_BET}")
        else:
            print("Please enter a number")
    return bets
def spin(balance):
    line = get_lines()
    while True:
        bet = get_bet()
        total_bet = bet * line
        if total_bet > balance:
            print(f"You do not have ${total_bet} to bet . Current balance is ${balance}")
        else:
            break
    print(f"You are betting ${bet} on  {line} lines. Total bet is ${total_bet}")

    slots=get_slot_machine_spin(ROWS,COLS,symbol_count)
    print_slot_machine(slots)
    winnings,winning_line=check_winings(slots,line,bet,symbol_value)
    print(f"you won ${winnings}")
    print(f"you won on line {winning_line}")
    return winnings-total_bet

# Defining main function so the function can continuously run
def main():
    balance = deposit()
    while True:
        print(f"Current balance ${balance}")
        answer= input("Press enter to play (q to quit).")
        if answer == "q":
            break
        balance = balance + spin(balance)
    print(f"You left with ${balance}")


main()
