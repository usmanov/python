from rock_paper_scissors_art import rock, paper, scissors
import random
gamer_choice = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.'))
if gamer_choice >= 3 or gamer_choice <=-1:
    print("You have entered the wrong number, You lose the game!")
else:
    choices = [rock,paper,scissors]
    print(choices[gamer_choice])

    computer_choice = random.choice(choices)
    print (f"Computer chose: \n{computer_choice}")

# Rock wins against scissors.
# Scissors win against paper.
# Paper wins against rock.

    if choices[gamer_choice] == rock and computer_choice == scissors:
        print("You win!")
    elif choices[gamer_choice] == scissors and computer_choice == paper:
        print("You win!")
    elif choices[gamer_choice] == paper and computer_choice == rock:
        print("You win!") 
    elif choices[gamer_choice] == computer_choice:
        print("Draw!")
    else:
        print("Computer wins")  
