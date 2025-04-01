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
        result = "tie"

    # There are three ways to win
    elif user == "paper" and comp == "rock":
        result = "win"
    elif user == "scissors" and comp == "paper":
        result = "win"
    elif user == "rock" and comp == "scissors":
        result = "win"
    # If it's not a win / tie, then it's a loss
    else:
        result = "lose"

    return result

# Main Routine Starts here

# Initialise game variables
mode = "regular"
rounds_played = 1

rps_list = ["rock", "paper", "scissors", "xxx"]


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
while rounds_played < num_rounds:

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
    print(f"{user_choice} vs {comp_choice}, {result}")
    rounds_played += 1


    # If users are in infinite mode, increase number of rounds!
    if mode == "infinite":
        num_rounds += 1




# Game loop ends here

# Game history / Statistics area