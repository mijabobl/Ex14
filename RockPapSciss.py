import random

def user_choice():
    choice = input("Select Option, \"r\" = Rock, \"p\" = Paper, \"s\" = Scissors : ")
    print()
    if choice == "r":
        choice = "Rock"
        return choice
    elif choice == "p":
        choice = "Paper"
        return choice
    elif choice == "s":
        choice = "Scissors"
        return choice
    else:
        print("Thats not a choice! you have wasted a game")

def comp_choice():
    comp = random.randint(0,2)
    if comp == 0:
        comp = "Rock"
        return comp
    elif comp == 1:
        comp = "Paper"
        return comp
    elif comp == 2:
        comp = "Scissors"
        return comp


def solution(you, cpu):
    if you == "Rock" and cpu == "Paper":
        print("Computer wins")
    elif you == "Paper" and cpu == "Paper":
        print("its a draw")
    elif you == "Scissors" and cpu == "Paper":
        print("You win")
    elif you == "Rock" and cpu == "Rock":
        print("its a draw")
    elif you == "Paper" and cpu == "Rock":
        print("You win")
    elif you == "Scissors" and cpu == "Rock":
        print("Computer wins")
    elif you == "Rock" and cpu == "Scissors":
        print("You win")
    elif you == "Paper" and cpu == "Scissors":
        print("Computer wins")
    elif you == "Scissors" and cpu == "Scissors":
        print("its a draw")
    else:
        print("Try and read the rules")


play = 0
print("Lets play 5 games of Rock Paper Scissors")
while play < 6:
    yourGo = user_choice()
    print("You Chose", yourGo)
    compGo = comp_choice()
    print("Computer Chose", compGo)
    solution(yourGo, compGo)
    print()
    play = play + 1

print("END OF GAME")






