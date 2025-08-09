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
rock_paper_scissors=[rock, paper, scissors]
clientChoice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n"))
if clientChoice > 2 or clientChoice < 0 :
    print("You typed invalid number , You loose!")
else:
    print(rock_paper_scissors[clientChoice])
    print("Computer choose:\n")
    computerChoice = random.choice(rock_paper_scissors)
    print(computerChoice)
    if rock_paper_scissors[clientChoice] == computerChoice:
        print("You Draw")
    elif (rock_paper_scissors[clientChoice] == rock and computerChoice == paper) or (
            rock_paper_scissors[clientChoice] == paper and computerChoice == scissors) or (
            rock_paper_scissors[clientChoice] == scissors and computerChoice == rock):
        print("You loose")
    else:
        print("You win")