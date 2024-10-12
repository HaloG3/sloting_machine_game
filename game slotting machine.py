import random
MAX_LINES = 3 # constant so we can use them anywhere in code
MAX_BET = 100
MIN_BET = 1


ROWS = 3
COLS = 3

symbol_count = {'A' : 2,
                'B' : 4,
                'C' : 6,
                'D' : 8,
                }
symbol_value = {'A' : 5,
                'B' : 4,
                'C' : 3,
                'D' : 2
}
def check_winnings(columns, lines , bet, values):
    winnings = 0
    winnings_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
            else:
                winnings +=values[symbol] * bet
                winnings_lines.append(line + 1)
        return winnings, winnings_lines

# machine spin code
def get_slot_machine_spin(rows,cols,symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range (cols):
        column =    []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)
    return columns

def print_slot_machine(columns):
    for row in range (len(columns[0])):
        for i, column in enumerate(columns):
            if i !=len(columns) -1:
                print(column[row], end= '    ~|~   ')
            else :
                print(column[row], end= '')
        print()
 cautions = (' These are some basic rules of game:-'
             'Enter the amount you want to deposit.'
             'Enter the number of line Which you want to BET on.'
             'Enter the money you want put on  each line.'
             'This programm is totally random so there is no cheating in this game'
             'In last you can see what amout is left in your balance ')

def deposit():
    while True:
        amount = input(f'{cautions}What would you like to deposit today? *CASH*: ')
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print('amount must be greater than 0.')
        else:
            print('Please enter a number.  ' )
    return amount


def get_number_of_lines ():
    while True:
        lines = input('Enter the number of lines to bet on. (1-'+ str(MAX_LINES)+ '): ') # when we add 2 string they got attached each other but MAX_LINES is number so they are added & we need attachemnent of lines
        if lines.isdigit():
            lines = int(lines)
            if 1<= lines <= MAX_LINES:
                break
            else:
                print(' Enter a valid number of lines. ')
        else:
            print('Please enter the number:- ')
    return lines

def get_bet():
    while True:
        amount = input (f'What *CASH* would you like to bet on EACH LINE ? ' )
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount<= MAX_BET:
                break
            else:
                print(f'Amount must be between ${MIN_BET} - ${MAX_BET}. ')
        else:
            print('please enter a number.')
    return amount
def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet*lines

        if total_bet > balance:
            print(f'You do not have enough to bet that amount, your current balance is: ${balance} ')
        else:
            break
    print(f'You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}')

    slots = get_slot_machine_spin(ROWS, COLS,symbol_count)
    print_slot_machine(slots)
    winnings, winnings_lines = check_winnings(slots,lines,bet,symbol_value)
    print(f'YOU WON ${winnings} !!! \n'*3 )
    print(f'You won on lines:', *winnings_lines)
    return winnings - total_bet

def main(): #  when the programm run over we can restart the program to play again
    balance = deposit()
    while True:
        print(f'current BALANCE is ${balance}')
        answer = input('Press Enter to Play[q to Quit]  ')
        if answer == 'q':
            break
        balance +=spin(balance)
    print(f'you left with ${balance}, you should paly one more time ')



main()