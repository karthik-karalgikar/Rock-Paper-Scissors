import random

game = ["r","p",'s']

playerchoice = input("Enter choice : ")


if playerchoice not in game:
    print("Error")
    quit()
comp = random.choice(game)
print("Player = ",playerchoice)
print("Computer = ",comp)
if(comp == 'r' and playerchoice == 'p'):
    print("player wins")
elif(comp == 'r' and playerchoice == 's'):
    print("Computer wins")
elif(comp == 'r' and playerchoice == 'r'):
    print("Rematch")
elif(comp == 'p' and playerchoice == 'r'):
    print("Computer wins")
elif(comp == 'p' and playerchoice == 's'):
    print("Player wins")
elif(comp == 'p' and playerchoice == 'p'):
    print("Rematch")
elif(comp == 's' and playerchoice == 'p'):
    print("Computer wins")
elif(comp == 's' and playerchoice == 'r'):
    print("Player wins")
elif(comp == 's' and playerchoice == 's'):
    print("Rematch") 
    

