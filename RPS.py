import random

user_input = input("Choose Rock, Paper, or Scissors: ")
computer_input = random.randint(0, 2)
if user_input == "Rock":
    if computer_input == 0:
        print("You Tied")
    elif computer_input == 1:
        print("You Lose")
    elif computer_input == 2:
        print("You Win")
elif user_input == "Paper":
    if computer_input == 0:
        print("You Win")
    elif computer_input == 1:
        print("You Tied")
    elif computer_input == 2:
        print("You Lose")
elif user_input == "Scissors":
    if computer_input == 0:
        print("You Lose")
    elif computer_input == 1:
        print("You Win")
    elif computer_input == 2:
        print("You Tied")
else:
    print("Wrong input")
