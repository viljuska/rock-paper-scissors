import random


def is_win(choice_1, choice_2):
    if choice_1 == 'r' and choice_2 == 's' or choice_1 == 'p' and choice_2 == 'r' or choice_1 == 's' and choice_2 == 'p':
        return True

    return False


class RPS:
    choices = ['r', 'p', 's']
    game_over = False

    def play(self):
        while not self.game_over:
            user_choice = input('Choose type:\n(r) rock\n(p) paper\n(s) scissors\n').lower()
            computer_choice = random.choice(self.choices)

            print(f"User choose {user_choice} and computer {computer_choice}")

            if user_choice == computer_choice:
                print('It\'s a tie')
            elif is_win(user_choice, computer_choice):
                print('User wins this round')
            else:
                print('Computer won this round')

            self.game_over = input('Do you want to play again? y/n\n').lower() == 'n'
