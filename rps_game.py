import random

options = ['rock', 'paper', 'scissors']
running = True

while running:
    player = input("Enter you choice: ")
    computer = random.choice(options)
    print(f"Your choice: {player}")
    print(f"Computer Choice: {computer}")
    
    if player == computer:
        print("TIE")
        #break

    if player == 'rock' and computer == 'paper':
        print("You Lose")
        #break

    if player == 'rock' and computer == 'scissors':
        print("You WIN")
        #break

    if player == 'paper' and computer == 'rock':
        print("You WIN")
        #break

    if player == 'paper' and computer == 'scissors':
        print("You Lose")
        #break

    if player == 'scissors' and computer == 'paper':
        print("You WIN")
        #break

    if player == 'scissors' and computer == 'rock':
        print("You Lose")
        #break

    play_again = input("Do you want to play again (y/n): ").lower()
    if not play_again == 'y':        
        running = False
print("Thanks for Playing")
     
    




