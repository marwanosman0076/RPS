import random

# functions go here
def statement_generator(statement, decoration):

    sides = decoration * 3

    statement = '{} {} {}'.format(sides, statement, sides)
    top_bottom = decoration * len(statement)

    print(top_bottom)
    print(statement)
    print(top_bottom)
    return ""
def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()

        if response == 'yes' or response == 'y':
            response = 'yes'
            return response
        elif response == 'no' or response == 'n':
            response = 'no'
            return response
        else:
            print ('please answer yes / no') 
def instructions() :
    print()
    print('**** How To Play ****')
    print()
    print('To play you must say how many rounds you would like to play with, once you have typed in the rounds you are to typle Rock (r) Paper (p) or scissors (s). once you do that you have a chance of winning. To win paper beats rock, rock beaths scissors, and scissors beat paper. The computer will pick a random object and will try to beat you. Good Luck.')
    print()
    return ''

print()
statement_generator("Welcome to Rock Paper Scissors", "*")
print()

played_before = yes_no('have you played the game before? ')

if played_before =='no':
    instructions()
else:
    print('Program Continues')
# checks for a number that is more than zero
def check_rounds():

    while True:
        response = input("How many rounds: ")

        round_error = "please type either <enter> or an interger that is more than 0"
        
        #if infinite mode no chosen, check response is an integer is more than 0
        if response != "":
            try:
                response = int(response)
                if response <1:
                    print(round_error)
                    continue
            except ValueError:
                print(round_error)
                continue
        return response

# checks user response based on a list of valid answers
def choice_checker(question, valid_list, error):


    valid = False
    while not valid:

        #ask user for choice (and put choice in lowercase)
        response = input(question).lower()
        # Iterates through list and if response is an item
        # in the list (or the first letter of an item), the
        # full item name is returned

        for item in valid_list:
            if response == item[0] or response == item:
                return item
        
        #output error if item not in list
        print(error)
        print()



#main routine goes here

# list of valid responses
yes_no_list = ["yes", "no"]
rps_list = ["rock", "paper", "scissors", "xxx"]

#ask user if they have played before
#if "yes", show instructions
choose_instructions = "please choose rock (r), paper (p), scissors (s)"
choose_error = "please choose from rock / paper / scissors (or xxx to quit)"

# ask user for # of rounds then loop...
rounds_played = 0
game_summary = []
rounds_lost= 0
rounds_drawn = 0



# ask user for # of rounds, <enter> for infinite mode
rounds = check_rounds()

end_game = "no"
while end_game == "no":
    #start of game play loop
    
    #rounds heading
    print()
    if rounds == "":
        heading = "continuous Mode: Round {}".format(rounds_played + 1)
        
    else:
        heading = "round {} of {}".format(rounds_played + 1, rounds)
        
    print(heading)

    #ask user for choice and check it's valid
    choose = choice_checker( choose_instructions, rps_list, choose_error)

    # get computer choice
    comp_choice = random.choice(rps_list[:-1])
    print("comp choice:", comp_choice) 

    #end game if exit code is typed
    if choose == "xxx":
        break

    # get computer choice
    comp_choice == random.choice(rps_list[:-1])

    #compare choices
    if comp_choice == choose:
        result = "tie"
        rounds_drawn += 1
    elif choose == "rock" and comp_choice == "scissors":
        result = "won"
    elif choose == "paper" and comp_choice == "rock":
        result = "won"
    elif choose == "scissors" and comp_choice == "paper":
        result = "won"
    else:
        result = "lost"
        rounds_lost += 1
    
    if result == "tie":
        feedback = "its a tie"
    else:
        feedback = "{} vs {} - you {}".format(choose, comp_choice, result)
    #output results
    print(feedback)
    rounds_played += 1
    # end game if requested # of rounds has been played
    if rounds_played == rounds:
        break


# quick calculations (stats)
rounds_won = rounds_played - rounds_lost - rounds_drawn


#***** calculate game stats *****
percent_win = rounds_won / rounds_played * 100
percent_lost = rounds_lost / rounds_played * 100
percent_tie = rounds_drawn / rounds_played * 100


print()

# displays game stats with % values to the nearest whole number
print("***** Game Statistics *****")
print("win: {}, ({:.0f}%)\nloss: {}, ({:.0f}%)\nTie: {}, ({:.0f}%)".format(rounds_won, percent_win, rounds_lost, percent_lost, rounds_drawn, percent_tie))

#end of game statements
print()
print("***** END GAME SUMMARY *****")
print()
print("Won: {} \t\t Lost: {} \t\t Draw: {}".format(rounds_won, rounds_lost, rounds_drawn))
print()
print("Thnaks for playing")


#ask user if they want to see their game history
#if "yes" show game history

