# Version 3 - error message included when calling function


# Function goes here
def choice_checker(question, error):
    
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
user_choice = ""
while user_choice !="xxx":

    # Ask user for choice and check it's valid
    user_choice = choice_checker("Choose rock/ paper / "
                                 "scissors (r/p/s): ",
                                 "Please choose from rock / "
                                 "paper / scissors "
                                 "(or xxx to quit)")
    
    # Print out choice for comparison purposes
    print ("You chose {}".format(user_choice))