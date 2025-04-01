
# Check that users have entered a valid
# option based on a list
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

#Main routine

# ask the user if they want instructions (check they say yes / no)
want_instructions = string_checker ("Do you want to read the instructions? ")

if want_instructions == "yes":
    instructions()

print()
print("Program continues")
