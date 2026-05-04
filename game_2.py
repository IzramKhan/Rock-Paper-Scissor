import random
import time

def description():
    print('''
          
╔═══════════════════════════════════════════════╗
║   🎮 WELCOME TO ROCK • PAPER • SCISSORS 🎮   ║
╚═══════════════════════════════════════════════╝

📜 RULES OF THE GAME:
 1️⃣ Rock     🪨 beats Scissors ✂️
 2️⃣ Paper    📄 beats Rock     🪨
 3️⃣ Scissors ✂️ beats Paper    📄
    
🎯 OPTIONS:
r -> Rock     🪨
p -> Paper    📄
s -> Scissors ✂️
    ''')

def animation(message):
    print('\n')
    for char in message:
        print(char, end='', flush=True)
        time.sleep(0.03)
    time.sleep(0.5)
    
def intro():
    animation('|| ** | * WELCOME TO ROCK • PAPER • SCISSORS | * ** ||')
    
def outro():
    animation('|| ** | * THANKS FOR PLAYING! SEE YOU NEXT TIME! | * ** ||')
    
class Messages:
    INVALID_ROUNDS = '\n❌ Invalid rounds! Enter a valid number!'
    INVALID_CHOICE = '\n❌ Invalid choice! Enter r, p, or s!'
    INVALID_NAME = '\n❌Invalid name! Name shouldbe in the range of (2 - 12)!'
    INVALID_CHOICE_ = '\n💔 Invalid choice! Enter (y or n)!'

def get_lst(plr_turn):
   
    if plr_turn == 'r':
        return ['s', 'r', 'p']
    elif plr_turn == 'p':
        return ['r', 'p', 's']
    elif plr_turn == 's':
        return ['p', 's', 'r']

def get_name():
    while True:
        name = input('\nEnter your name: ')
        if 1 < len(name) <= 12:
            return name
        print(Messages.INVALID_NAME)
        
def get_rounds():
    while True:
        try:
            rounds = int(input('\nEnter number of ROUNDS: '))
            if rounds > 0:
                return rounds
            print(Messages.INVALID_ROUNDS)
        except ValueError:
            print(Messages.INVALID_ROUNDS)
        
def computer_turn():
    return random.choice(['r', 'p', 's'])

def player_turn():
    while True:
        choice = input('\nEnter you choice: ').lower().strip()
        if choice in {'r', 'p', 's'}:
            return choice
        print(Messages.INVALID_CHOICE)

def show_rounds(rounds):
    print(f'\n{"-" * 25} ROUND {rounds} {"-" * 25}')
    
def show_winner(winner):
    time.sleep(0.5)
    if winner:
        print(f'\n{winner.title()} won this round! 🏆')    
    else: 
        print(f'\nThis rounds ends in a tie!')
    
def show_choice(plr_ch, comp_ch):
    choices = {'r': 'Rock 🪨', 'p': 'Paper 📄', 's': 'Scissors ✂️'}
    print(f'\n{'Your choose: ':<16}: {choices[plr_ch]}')
    time.sleep(0.5)
    print(f'{'Computer choose':<16}: {choices[comp_ch]}')
    
def final_result(plr_pts, comp_pts, ties):
    time.sleep(0.5)
    print('\n' + '-' * 60)
    print(f'Player Points: {plr_pts} | Computer Points: {comp_pts} | TIES: {ties}')
    print('-' * 60)
    
    if plr_pts > comp_pts:
        print('\nCongragulations! You have won the game! 🏆🔥')
    elif plr_pts < comp_pts:
        print('\nOH NO! You have lost! Computer have won the game! 💔')
    else:
        print('\nBoth points were equal at the end! This game is a tie!')    

def play_again():
    while True:
        choice = input('\nEnter do you want to play again (y/n): ').lower().strip()
        if choice == 'y':
            play_game()
        elif choice == 'n':
            return  outro()
        else:
            Messages.INVALID_CHOICE_
            
def play_game():
    
    name = get_name()
    rounds = get_rounds()
    plr_pts = 0
    comp_pts = 0
    ties = 0
    winner = None
    
    while rounds > 0:
        show_rounds(rounds)
        plr_ch = player_turn()
        comp_ch = computer_turn()
        lst = get_lst(plr_ch)
                
        if plr_ch == comp_ch:
            ties += 1
            
        elif lst.index(plr_ch) > lst.index(comp_ch):
            plr_pts += 1
            winner = name
            
        else:
            comp_pts += 1
            winner = 'computer'
            
        show_choice(plr_ch, comp_ch)
        show_winner(winner)

        rounds -= 1
    final_result(plr_pts, comp_pts, ties)
        
def main():
    intro()
    description()
    play_game()
    
    play_again()
    
if __name__ == '__main__':
    main()
            