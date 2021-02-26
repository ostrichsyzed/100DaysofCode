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

ropasc = [rock, paper, scissors]

print("Rock, paper, scissors againist the master!")
player = int(input("Type 0 for rock, 1 for paper, 2 for scissors. "))
print(ropasc[player])

AI = random.randint(0, 2)
print("AI picks: ")
print(ropasc[AI])

if player == 0 and AI == 2:
  print("Player wins!")

elif player == 1 and AI == 0:
  print("Player wins!") 
  
elif player == 2 and AI == 1:
  print("Player wins!")

else:
  print("Computer wins!")
