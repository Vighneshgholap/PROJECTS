##########################################################################################
## This is my first project where I will be building a rock, paper and scissor game!!   ##
## @SilentShroudedSteps                                                                 ##
##########################################################################################


import random
# for asking user if they wants to play again.
while True:
    choices = ["rock", "paper", "scissor"]  # three choices
    comp = random.choice(choices)           # computer chooses its hand
    player = None   

    while player not in choices:            # asking user to choose their hand
        player = input("rock, paper or scissor?: ").lower()

    if player == comp:                      # when its a tie
        print("Player: ", player)
        print("Computer: ", comp)
        print("It's a Tie!")
    elif (player == "paper" and comp == "rock") or (player == "rock" and comp =="scissor") or (player == "scissor" and comp =="paper"): # when player wins
        print("Player: ", player)
        print("Computer: ", comp)
        print("Player Wins!")
    else:                                    # when Computer wins
        print("Player: ", player)
        print("Computer: ", comp)
        print("Computer Wins!")
    
    play_again = input("Do you want to play again? (yes/no): ").lower()

    if play_again != "yes":
        break

print("It was fun! Bye!!")                   # end statement!