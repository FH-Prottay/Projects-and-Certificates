2#rock paper scissor problem
import random
Rock ="""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
Paper="""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
Scissors="""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
user= int(input('''rock=0 scissor=1 paper=2 \nwhat will you choose? '''))
if (user>=3 or user<0):
    print("enter correct number")
else:
    computer = random.randint(0, 2)
    print(f"computer chose {computer}")

    if (user == computer):
        if(user==0):
            print(f"{Rock} \t {Rock}")
            print(("draw"))
        elif(user==1):
            print(f"{Scissors} \t {Scissors}")
            print(("draw"))
        elif (user == 2):
            print(f"{Paper} \t {Paper}")
            print(("draw"))

    elif (user == 0 and computer == 2):
        print(f"{Rock} \t {Paper}")
        print("you lose")
    elif (user == 2 and computer == 0):
        print(f"{Paper} \t {Rock}")
        print("you won")
    elif (user < computer):
        if(user== 0 and computer == 1):
            print(f"{Rock} \t {Scissors}")
        elif (user== 1 and computer == 2):
            print(f"{Scissors} \t {Paper}")
        print("you won")
    elif (user > computer):
        if (user == 1 and computer == 0):
            print(f"{Scissors} \t {Rock}")
        elif (user == 2 and computer == 1):
            print(f"{Paper} \t {Scissors}")
        print("you lose")


