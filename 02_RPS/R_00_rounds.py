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

# Main Routine Starts here

# Initialise game variables
mode = "regular"
rounds_played = 1


print("🗿🧻✂️ Rock / Paper / Scissors Game 🗿🧻✂️")
print()

# Instructions

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
    print()

    # get user choice
    user_choice =  input("Choose: ")

    # If user choice is the exit code, break the loop
    if user_choice == "xxx":
        break


    rounds_played += 1


    # If users are in infinite mode, increase number of rounds!
    if mode == "infinite":
        num_rounds += 1




# Game loop ends here

# Game history / Statistics area