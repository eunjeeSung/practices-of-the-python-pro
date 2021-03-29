'''
# Shoddy procedural code
import random

options = ['rock', 'paper', 'scissors']
print('(1) Rock\n(2) Paper\n(3) Scissors')
human_choice = options[int(input('Enter the number of your choice: ')) - 1]
print(f'You chose {human_choice}')
computer_choice = random.choice(options)
print(f'The computer chose {computer_choice}')
if human_choice == 'rock':
    if computer_choice == 'paper':
        print('Sorry, paper beat rock')
    elif computer_choice == 'scissors':
        print('Yes, rock beat scissors!')
    else:
        print('Draw!')
elif human_choice == 'paper':
    if computer_choice == 'scissors':
        print('Sorry, scissors beat paper')
    elif computer_choice == 'rock':
        print('Yes, paper beat rock!')
    else:
        print('Draw!')
elif human_choice == 'scissors':
    if computer_choice == 'rock':
        print('Sorry, rock beat scissors')
    elif computer_choice == 'paper':
        print('Yes, scissors beat paper!')
    else:
        print('Draw!')
'''

import random

OPTIONS = ['rock', 'paper', 'scissors']
WINNING_OPTIONS = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}

def print_options():
    print('\n'.join(f"({i+1}) {option.capitalize()}" \
        for i, option in enumerate(OPTIONS)))

def get_human_choice():
    human_choice = OPTIONS[int(input('Enter the number of your choice: ')) - 1]
    print(f'You chose {human_choice}')
    return human_choice

def get_computer_choice():
    computer_choice = random.choice(OPTIONS)
    print(f'The computer chose {computer_choice}')
    return computer_choice

def get_human_wins(human_choice, computer_choice):
    if human_choice == computer_choice:
        return 'Draw'
    elif WINNING_OPTIONS[human_choice] == computer_choice:
        return 'Win'
    elif WINNING_OPTIONS[computer_choice] == human_choice:
        return 'Lose'

def print_result(human_choice, computer_choice):
    result = get_human_wins(human_choice, computer_choice)
    if result == 'Win':
        print(f'Yes, {human_choice} beat {computer_choice}!')
    elif result == 'Lose':
        print(f'Sorry, {computer_choice} beat {human_choice}')        
    elif result == 'Draw':
        print(f'Draw!')

print_options()
human_choice = get_human_choice()
computer_choice = get_computer_choice()
print_result(human_choice, computer_choice)