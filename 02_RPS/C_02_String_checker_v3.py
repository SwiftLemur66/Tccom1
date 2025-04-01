def int_check():
    """checks users enter an integer more than / equal to 13"""

    error = "please enter an integer more than / equal to 13."

    while True:
        try:
            response = int(input("what is the game goal? "))

            if response < 13:
                print(error)
            else:

                return response

        except ValueError:
            print(error)

        # print error is user does not enter something that is valid
        print(error)
        print()


# Main routine goes here

rps_list = ["rock", "paper", "scissors", "xxx"]

want_instructions = int_check("Do you want to see the instructions? ")

print("you chose: ", want_instructions)

user_choice = int_check("choose:", rps_list)
print("You chose: ", user_choice)