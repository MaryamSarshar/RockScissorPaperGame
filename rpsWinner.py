def rpsWinner(player1,computer):
    if player1 == "rock" and computer == "scissore":
        return "player one"
    elif player1 == "scissore" and computer == "rock":
        return "computer"
    elif player1 == "paper" and computer == "scissore":
        return "computer"
    elif player1 == "scissore" and computer == "paper":
        return "player one"
    elif player1 == "paper" and computer == "rock":
        return "player one"
    elif player1 == "rock" and computer == "paper":
        return "computer"
    else:
        return "tie"
import random
def computerInput():
    computer = ["rock", "scissore","paper"]
    for i in computer:
        input_computer = random.choice(computer)
        return input_computer

player1 = input("choose one of these: rock , scissore or paper: ")
computer = computerInput()
winner = rpsWinner(player1 , computer)
print("player one : "+ player1 ,"\n"+"computer: "+computer)
print("The winner is ", winner)
