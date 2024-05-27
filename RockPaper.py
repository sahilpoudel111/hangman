import random
rock='''
      __________
-----(_________)
    (__________)
    (_________)
    (_________)
----(_______)
'''
paper='''
      _________________
-----(________________)
    (_________________)
    (__________________)
    (________________)
----(______________)
'''
scissor='''
      _______
-----(______)
    (________________)
    (________________)
    (_________)
----(_______)
'''
game_images = [rock, paper, scissor]
user_choice = int(input("Enter your choice: Type 0 for Rock, 1 for Paper, 2 for Scissor"))
if user_choice >= 3 or user_choice < 0:
    print("you entered invalid number, try again")
else:
    print(game_images[user_choice])
    computer_choice=random.randint(0,2)
    print("Computer chose:")
    print(game_images[computer_choice])
    if computer_choice == user_choice:
        print("It's a draw")
    elif user_choice == 2 and computer_choice == 0:
        print("You lose")
    elif user_choice == 0 and computer_choice == 2:
        print("You win")
    elif computer_choice > user_choice:
        print("You lose")
    elif user_choice > computer_choice:
        print("You win.")


