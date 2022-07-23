import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
uchoice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors."))
rpc = [rock,paper,scissors]
print(rpc[uchoice])
comp_choice = random.randint(0,2)
print("computer choose")
print(rpc[comp_choice])

if uchoice>=3 or uchoice<0:
	print("invalid input")
elif uchoice == 0 and comp_choice == 2:
	print('You win')
elif comp_choice == 0 and uchoice == 2:
	print("You loose")
elif uchoice > comp_choice:
	print("You Win")
elif comp_choice > uchoice:
	print("You loose")
elif uchoice == comp_choice:
	print("It's a draw")





