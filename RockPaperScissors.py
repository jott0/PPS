import random
def compvsplayer():
    user_action = input("Enter a choice (rock, paper, scissors): ")
    if user_action in ('rock','paper','scissors'):
        possible_actions = ["rock", "paper", "scissors"]
        computer_action = random.choice(possible_actions)
        print("\nYou chose",user_action,", computer chose",computer_action,"\n")
        if user_action == computer_action:
            print("Both players selected",user_action,"\nIt's a tie!")
        elif user_action == "rock":
            if computer_action == "scissors":
                print("Rock smashes scissors! You win!")
            else:
                print("Paper covers rock! You lose.")
        elif user_action == "paper":
            if computer_action == "rock":
                print("Paper covers rock! You win!")
            else:
                print("Scissors cuts paper! You lose.")
        elif user_action == "scissors":
            if computer_action == "paper":
                print("Scissors cuts paper! You win!")
            else:
                print("Rock smashes scissors! You lose.")
        e=input("Do you wish to continue PLAYER V/S COMPUTER MODE?(y/n): ")
        if e=='y' or e=='Y':
            compvsplayer()
    else:
        print("Invalid choice entered!")

def p1vsp2():
    user1_action= input("Player 1 enter a choice (rock, paper, scissors): ")
    user2_action=input("Player 2 enter a choice (rock, paper, scissors): ")
    if user1_action in ('rock','paper','scissors') and user2_action in ('rock','paper','scissors'):
        print("\nPlayer 1 chose",user1_action,"Player 2 chose",user2_action,"\n")
        if user1_action == user2_action:
            print("Both players selected",user1_action,"\nIt's a tie!")
        elif user1_action == "rock":
            if user2_action == "scissors":
                print("Rock smashes scissors! Player 1 wins!")
            else:
                print("Paper covers rock! Player 2 wins.")
        elif user1_action == "paper":
            if user2_action == "rock":
                print("Paper covers rock! Player 1 wins!")
            else:
                print("Scissors cuts paper! Player 2 wins.")
        elif user1_action == "scissors":
            if user2_action == "paper":
                print("Scissors cuts paper! Player 1 wins!")
            else:
                print("Rock smashes scissors! Player 2 wins!")
        e=input("Do you wish to continue PLAYER 1 V/S PLAYER 2 MODE?(y/n): ")
        if e=='y':
            p1vsp2()
    else:
        print("Invalid choice entered!")
    
    
print("-------------------------------------------")
print("               GAME MENU\n")
print("To play in PLAYER V/S COMPUTER mode enter 1")
print("To play in PLAYER V/S PLAYER mode enter 2")
print("-------------------------------------------")
choice=int(input("Enter the choice: "))
if choice==1:
    compvsplayer()
elif choice==2:
    p1vsp2()
else:
    print("Invalid choice entered!!")
c='true'
while c=='true':
    w=input("Do you wish to continue playing ?(y/n): ")
    if w=='y' or w=='Y':
        print("-------------------------------------------")
        print("               GAME MENU\n")
        print("To play in PLAYER V/S COMPUTER mode enter 1")
        print("To play in PLAYER V/S PLAYER mode enter 2")
        print("-------------------------------------------")
        choice=int(input("Enter the choice: "))
        if choice==1:
            compvsplayer()
        elif choice==2:
                p1vsp2()
    else:
        print("THANK YOU FOR PLAYING.")
        c='false'
