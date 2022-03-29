# Function goes here
def choice_checker(question):

    errror = "Please choose from rock / paper / " \
        "sissors (or xxx to quit)"
        
    valid = False
    while not valid:

        #Ask user for choice (and put choice in lowercase)
        response = input(question).lower()

        if response == "r" or response == "rock":
            return response
        elif response == "p" or response == "paper":
            return response
        elif response == "s" or response == "scissors":
            return response
        
        # check for exit code...
        elif response == "xxx":
            return response
        else:
            print(error)

# Main routine goes here

# Loop for testing purposes
user_choice =