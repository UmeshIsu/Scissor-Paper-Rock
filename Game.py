import random
import time

def get_user_input():
    while True:
        user_input  = input("Choose rock, 'scissor', 'paper' or 'exit': ").lower()
        if user_input in ["rock","scissor","paper","exit"]:
            return user_input
        else:
            print("Invalid input. Please try again")

def determine_winner(user_input,computer_input):
    if user_input == computer_input:
        return "tie"
    elif (user_input == "rock" and computer_input == "scissor") or (user_input == "paper" and computer_input == "rock")  or (user_input == "scissor"  and computer_input == "paper"):
        return "user"
    else:
        return "computer"
    
def display_result(user_input,computer_input,winner):
    print(f"Your input is {user_input}")
    time.sleep(0.5)
    print(f"computer input is {computer_input}")
    time.sleep(0.5)

    if winner == "tie":
        print("Game tied!")
    elif winner == "user":
        print("You win!")
    else:
        print("computer wins!")

def main():
    user_points = 0
    computer_points = 0
    options = ["rock","scissor","paper"]

    while True:
        user_input = get_user_input()

        if user_input == "exit":
           print("Game ended!")
           time.sleep(0.5)
           print(f"Your last point is {user_points} and Computer last point is {computer_points}")
           break

        computer_input = random.choice(options)
        winner = determine_winner(user_input,computer_input)
        display_result(user_input,computer_input,winner)

       

        if winner == "user":
            user_points += 1
        elif winner == "computer":
            computer_points += 1

main()