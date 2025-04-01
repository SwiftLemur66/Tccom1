import random


def string_checker(question, valid_ans=('yes', 'no')):

    error = f"Please enter a valid option from the following list: {valid_ans}"

    while True:

        user_response = input(question).lower()

        for item in valid_ans:
            # check if the user response is a word in the list
            if item == user_response:
                return item

            #check if the user response is the same as
            # the first letter of an item in the list
            elif user_response == item[0]:
                return item

        # print error is user does not enter something that is valid
        print(error)
        print()



# Check for an integer more than 0 (allows <enter>)

def int_check(question):
    """checks users enter an integer that is 1 or more"""

    while True:
        error = "please enter an integer that is 1 or more."

        to_check = input(question)

        # check fot infinite mode
        if to_check == "":
            return "infinite"

        try:
            response = int(to_check)

            if response < 1:
                print(error)
            else:
                return response

        except ValueError:
            print(error)

# compares user / computer choice and returns
# result (win / lose / tie)
def rps_compare(user, comp):

    # If the user and the computer choice is the same, it's a tie
    if user == comp:
        round_result = "tie"

    # There are three ways to win
    elif user == "paper" and comp == "rock":
        round_result = "win"
    elif user == "scissors" and comp == "paper":
        round_result = "win"
    elif user == "rock" and comp == "scissors":
        round_result = "win"
    # If it's not a win / tie, then it's a loss
    else:
        round_result = "lose"

    return round_result

# Main Routine Starts here

# Initialise game variables
mode = "regular"

rounds_played = 1
rounds_tied = 1
rounds_lost = 1

rps_list = ["rock", "paper", "scissors", "xxx"]
game_history = []

print("🗿🧻✂️ Rock / Paper / Scissors Game 🗿🧻✂️")
print()

# Ask user if they want to see the instructions and display
# them if requested
def instructions():
    """Prints instructions"""

    print("""
    **** INSTRUCTIONS! ****   

    To begin, choose the number of rounds (or infinite mode).

    Then play against a computer. You need to choose R (Rock),
    P (Paper) or S (Scissors).


THe rules are as followed:
- Paper beats Rock
- Rock beats Scissors
- Scissors beat Paper""")

want_instructions = input("do you want to read the instructions? ")
if want_instructions == "yes":
                instructions()

# Check user enters yes (y) or no (n)



# Ask user for number of rounds / infinite mode
num_rounds = int_check("How many rounds would you like? Press enter for infinite mode: ")

if num_rounds == "infinite":
    mode = "infinite"

    num_rounds = 5

# Game loop starts here
while rounds_played <= num_rounds:

    # Rounds headings (based on mode)
    if mode == "infinite":
        rounds_heading = f"\n✂️🧻🗿 Rounds {rounds_played} (Infinite Mode) 🗿🧻✂️"
    else:
        rounds_heading = f"\n👾👾👾 Rounds {rounds_played} of {num_rounds} 👾👾👾"


    print(rounds_heading)


    #randomly choose from the rps list (excluding the exit code)
    comp_choice = random.choice(rps_list[:-1])
    print("Computer choice", comp_choice)

    # get user choice
    user_choice =  string_checker("Choose: ", rps_list)
    print("you chose", user_choice)

    # If user choice is the exit code, break the loop
    if user_choice == "xxx":
        break

    result = rps_compare(user_choice, comp_choice)

    # Adjust game lost / game tied counters and add results to game history
    if result == "tie":
        rounds_tied += 1
        feedback = "It's a draw!"
    elif result == "lose":
        rounds_lost += 1
        feedback = "Bro lost"
    else:
        feedback = "You won!"

    # Set up round feedback and output its user
    # Add it to the game history list (include the round number)
    round_feedback = f"{user_choice} vs {comp_choice}, {feedback}"
    history_item = f"Round: {rounds_played} - {round_feedback}"

    print(round_feedback)
    game_history.append(history_item)
    rounds_played += 1
    # If users are in infinite mode, increase number of rounds!
    if mode == "infinite":
        num_rounds += 1




# Game loop ends here

# Game history / Statistics area
rounds_won = rounds_played - rounds_tied - rounds_lost
percent_won = rounds_won / rounds_played * 100
percent_lost = rounds_lost / rounds_played * 100
percent_tied = 100 - percent_won - percent_lost

# Output Game Statistics
print("👾👾👾-Game Statistics-💀💀💀")
print(f"🏆 Won: {percent_won: .2f} \t "
      f"💀 Lost: {percent_lost: .2f} \t"
      f"🪢 Tied: {percent_tied: .2f} \t")

want_history = string_checker("Do you want to see your game history? ")
if want_history == "yes":
    print("Game History")

    for item in game_history:
        print(item)