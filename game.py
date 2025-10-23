import random
import time

player_name = input('Enter your name: ').strip().title()
print('''
╔═══════════════════════════════════════════════╗
║   🎮 WELCOME TO ROCK • PAPER • SCISSORS 🎮   ║
╚═══════════════════════════════════════════════╝
''')

rules = '''
📜 RULES OF THE GAME:
1️⃣ Rock 🪨 beats Scissors ✂️
2️⃣ Paper 📄 beats Rock 🪨
3️⃣ Scissors ✂️ beats Paper 📄
'''
player_options = '''
🎯 OPTIONS:
r → Rock 🪨
p → Paper 📄
s → Scissors ✂️
'''
quit_option = '''
🚪 Play as many rounds as you like — press "q" to quit anytime.
'''

print(rules)
print(player_options)
print(quit_option)

def processing_dot_animation(message='Loading', delay=0.4):
    print(f'\n{message}', end='', flush=True)
    for i in range(3):
        print('.', end='', flush=True)
        time.sleep(delay)
    print()

player_points = []
computer_points = []
options = ['r', 'p', 's']
round_number = 1
no_of_ties = 0

while True:
    computer_choice = random.choice(options)
    print(f'\n{"─" * 25} ROUND {round_number} {"─" * 25}')
    player_choice = input('\n👉 Enter your choice: ').lower().strip()

    if player_choice == 'r' and computer_choice == 's':
        processing_dot_animation('Calculating Result')
        print('\n🪨 Your choice: Rock')
        print('✂️ Computer choice: Scissors\n')
        print(f'🏆 Winner of this round: {player_name} 👏🎉')
        player_points.append(1)
        round_number += 1

    elif player_choice == 'r' and computer_choice == 'p':
        processing_dot_animation('Calculating Result')
        print('\n🪨 Your choice: Rock')
        print('📄 Computer choice: Paper\n')
        print('🤖 Winner of this round: Computer 🎉')
        computer_points.append(1)
        round_number += 1

    elif player_choice == 'p' and computer_choice == 'r':
        processing_dot_animation('Calculating Result')
        print('\n📄 Your choice: Paper')
        print('🪨 Computer choice: Rock\n')
        print(f'🏆 Winner of this round: {player_name} 👏🎉')
        player_points.append(1)
        round_number += 1

    elif player_choice == 'p' and computer_choice == 's':
        processing_dot_animation('Calculating Result')
        print('\n📄 Your choice: Paper')
        print('✂️ Computer choice: Scissors\n')
        print('🤖 Winner of this round: Computer 🎉')
        computer_points.append(1)
        round_number += 1

    elif player_choice == 's' and computer_choice == 'p':
        processing_dot_animation('Calculating Result')
        print('\n✂️ Your choice: Scissors')
        print('📄 Computer choice: Paper\n')
        print(f'🏆 Winner of this round: {player_name} 👏🎉')
        player_points.append(1)
        round_number += 1

    elif player_choice == 's' and computer_choice == 'r':
        processing_dot_animation('Calculating Result')
        print('\n✂️ Your choice: Scissors')
        print('🪨 Computer choice: Rock\n')
        print('🤖 Winner of this round: Computer 🎉')
        computer_points.append(1)
        round_number += 1

    elif player_choice == computer_choice:
        processing_dot_animation('Calculating Result')
        print('\n🟰 It’s a tie!')
        print('You both chose:',
              '🪨 Rock' if player_choice == 'r' else
              '📄 Paper' if player_choice == 'p' else
              '✂️ Scissors')
        print('No points awarded this round.')
        round_number += 1
        no_of_ties += 1

    elif player_choice == 'q':
        print('\n💨 You chose to quit the game.\n')
        print('🎯 FINAL RESULTS 🎯')
        print('─────────────────────────────')
        print(f'🧾 Total Rounds Played: {round_number - 1}')
        print(f'🤝 Ties: {no_of_ties}')
        print(f'🏅 {player_name}: {sum(player_points)}')
        print(f'💻 Computer: {sum(computer_points)}')
        print('─────────────────────────────')

        if sum(player_points) > sum(computer_points):
            print(f'\n🏆 Congratulations {player_name}! You won the game! 🎉')
        elif sum(player_points) < sum(computer_points):
            print('\n💻 The Computer takes the win this time! 😎')
        else:
            print('\n🟰 The game ends in a perfect tie! 🟰')

        play_again = input("\n🔁 Do you want to play again? (y/n): ").lower()
        if play_again == 'y':
            player_points.clear()
            computer_points.clear()
            round_number = 1
            no_of_ties = 0
            print('\n✨ Restarting the game... ✨')
            time.sleep(1)
            continue
        else:
            print("\n👋 Thanks for playing! See you next time!")
            break

    else:
        print('\n❌ Invalid input!')
        print('Please enter only: r, p, s, or q.')

# ____________________________________THE-END____________________________________
# Created by: Izram Khan
# Date created: 23-Oct-2025
