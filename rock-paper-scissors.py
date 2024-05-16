import random 

charac=("paper","rock","scissors")
computer=random.choice(charac)

player=input("Enter a choice (rock,paper,scissors):")

if (player=="rock" or player=="paper" or player=="scissors"):
    print(f"Player:{player}")
    print(f"Computer:{computer}")
else:
    print("Choose from provided options...")

if (player==computer):
    print("Game:Tie")
elif(player=="scissors" and computer=="rock"):
    print("Computer wins")
elif(player=="paper" and computer=="rock"):
    print("Player wins")
elif(player=="scissors" and computer=="paper"):
    print("Player wins")
elif(computer=="scissors" and player=="rock"):
    print("Player wins")
elif(computer=="paper" and player=="rock"):
    print("Computer wins")
elif(computer=="scissors" and player=="paper"):
    print("Computer wins")
