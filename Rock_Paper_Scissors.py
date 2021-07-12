#This is a game of rock, paper, scisors between you and the computer.
#This program also keeps the count of scores and prints the final result.
import random
import math
def play():
    user_choice = input("Enter your choice: r for rock, p for paper, s for scissors \n")
    user_choice.lower()
    computer_choice = random.choice(['r', 'p', 's'])

    if user_choice == computer_choice:
        return (0, user_choice, computer_choice)

    # r > s, s > p, p > r
    if user_win(user_choice, computer_choice):
        return (1, user_choice, computer_choice)

    return (-1, user_choice, computer_choice)

def user_win(player, opponent):
    #if player has won against opponent
    if (player == 'r' and opponent == 's') or (player == 'p' and opponent == 'r') or (player == 's' and opponent == 'p'):
        return True
    else:
        return False

#function to keep a count of scores
def play_best_of(n):
    player_wins = 0
    computer_wins = 0
    wins_necessary = math.ceil(n/2)
    while player_wins < wins_necessary and computer_wins < wins_necessary:          #tie
        result, user_choice, computer_choice = play()
        # tie
        if result == 0:
            print('It is a tie. You and the computer have both chosen {}. \n'.format(user_choice))
        # you win
        elif result == 1:
            player_wins += 1
            print('You chose {} and the computer chose {}. You won!\n'.format(user_choice, computer_choice))
        else:
            computer_wins += 1
            print('You chose {} and the computer chose {}. You lost :(\n'.format(user_choice, computer_choice))
    if player_wins > computer_wins:
        print('*' * 20)
        print('You have won {} of {} games! What a champ :D'.format(player_wins,n))
        print('*' * 20)
    else:
        print('*' * 20)
        print('Unfortunately, the computer has won {} of {} games. Better luck next time!'.format(computer_wins,n))
        print('*' * 20)

play_best_of(3)


