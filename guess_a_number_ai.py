import random
import math

# Justin H
# config
default_low = 1
default_high = 100



# helper functions
def show_start_screen():
    print("""
 _______  __   __  _______  _______  _______    _______    __    _  __   __  __   __  _______  _______  ______      _______        ___        
|       ||  | |  ||       ||       ||       |  |   _   |  |  |  | ||  | |  ||  |_|  ||  _    ||       ||    _ |    |   _   |      |   |       
|    ___||  | |  ||    ___||  _____||  _____|  |  |_|  |  |   |_| ||  | |  ||       || |_|   ||    ___||   | ||    |  |_|  |      |   |       
|   | __ |  |_|  ||   |___ | |_____ | |_____   |       |  |       ||  |_|  ||       ||       ||   |___ |   |_||_   |       |      |   |       
|   ||  ||       ||    ___||_____  ||_____  |  |       |  |  _    ||       ||       ||  _   | |    ___||    __  |  |       | ___  |   |  ___  
|   |_| ||       ||   |___  _____| | _____| |  |   _   |  | | |   ||       || ||_|| || |_|   ||   |___ |   |  | |  |   _   ||   | |   | |   | 
|_______||_______||_______||_______||_______|  |__| |__|  |_|  |__||_______||_|   |_||_______||_______||___|  |_|  |__| |__||___| |___| |___| 
    """)

def show_credits():
    print()
    print("""
███╗   ███╗ █████╗ ██████╗ ███████╗    ██████╗ ██╗   ██╗         ██╗██╗   ██╗███████╗████████╗██╗███╗   ██╗    ██╗  ██╗ █████╗ ████████╗██╗     ███████╗██╗   ██╗
████╗ ████║██╔══██╗██╔══██╗██╔════╝    ██╔══██╗╚██╗ ██╔╝         ██║██║   ██║██╔════╝╚══██╔══╝██║████╗  ██║    ██║  ██║██╔══██╗╚══██╔══╝██║     ██╔════╝╚██╗ ██╔╝
██╔████╔██║███████║██║  ██║█████╗      ██████╔╝ ╚████╔╝          ██║██║   ██║███████╗   ██║   ██║██╔██╗ ██║    ███████║███████║   ██║   ██║     █████╗   ╚████╔╝ 
██║╚██╔╝██║██╔══██║██║  ██║██╔══╝      ██╔══██╗  ╚██╔╝      ██   ██║██║   ██║╚════██║   ██║   ██║██║╚██╗██║    ██╔══██║██╔══██║   ██║   ██║     ██╔══╝    ╚██╔╝  
██║ ╚═╝ ██║██║  ██║██████╔╝███████╗    ██████╔╝   ██║       ╚█████╔╝╚██████╔╝███████║   ██║   ██║██║ ╚████║    ██║  ██║██║  ██║   ██║   ███████╗███████╗   ██║   
╚═╝     ╚═╝╚═╝  ╚═╝╚═════╝ ╚══════╝    ╚═════╝    ╚═╝        ╚════╝  ╚═════╝ ╚══════╝   ╚═╝   ╚═╝╚═╝  ╚═══╝    ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚══════╝   ╚═╝                                                                                                                                                               
    """)

def find_limit(current_high, current_low):
    limit = math.ceil(math.log((current_high - current_low) + 1, 2))
    return limit
    
def get_guess(current_low, current_high):
    guess = ( current_high + current_low)//2
    return guess

def decide_number(default_low,default_high):
    print()
    decide_1 = input("Hello " + str(name) + ", would you like to pick the numbers for your game? ")
    decide_1 = decide_1.lower()
    if decide_1 in ["yes","y","yeah","yep", ]:
        print()
        low = input("What is the lowest value for of number? ")
        low = int(low)
        print()
        high = input("What is the highest value of your number? ")
        high = int(high)
        
    else:
        print("That's fine we will just use default settings.")
        print()
        low = default_low
        high = default_high

    return low,high

def pick_number (current_low, current_high):
    print()
    print (name + " think of a number between " + str(current_low) + " and " + str(current_high) + ".")
    print("Press 'Enter' when ready...")
    useless_1 = input ()
  

def check_guess(guess,tries,limit):
    print("Is the number....")
    print(str(guess) + "?")
    print("I have guessed " + str(tries) + "/" + str(limit) + " times")
    test = input("Tell me if my number was too high, too low, or right, " + name + ". " )
    test = test.lower()
    print()
    
    if test in ["low", "higher","too low", "l"]:
        check = 1
        return check
    if test in ["high", "lower", "too high", "h"]:
        check = -1
        return check
    if test in ["right", "correct", "yes", "y"]:
        check = 0
        return check
    else:
        print("Enter a valid repsponse please.")
      

def show_result(guess,tries,limit):
    print()
    print("I guessed your number in only " + str(tries) + "/" + str(limit) + " tries.")
    print()
    print("Your number was " + str(guess) + " that was too easy.")
    print("C'mon " + name + ", you know you can't beat me.")
 

def play_again(name):
    while True:
        print()
        decision = input("Would you like to play again " + name + "? (y/n) ")
        decision = decision.lower()

        if decision == 'y' or decision == 'yes':
            print()
            return True
        elif decision == 'n' or decision == 'no':
            print()
            print("Goodbye. Good luck " + name + " on whatever you do.")
            return False
        else:
            print("I don't understand. Please enter 'y' or 'n'.")

def play(name):
    current_low, current_high = decide_number(default_low,default_high)
    check = -1
    tries = 1

    pick_number(current_low, current_high)
    limit = find_limit(current_high,current_low)
    
    while check != 0:
        guess = get_guess(current_low, current_high)
        check = check_guess(guess,tries,limit)

        if check == -1:
            current_high = guess
         
        elif check == 1:
            current_low = guess

        tries +=1

    show_result(guess,tries,limit)


# Game starts running here
show_start_screen()

playing = True

while playing:
    name = input("Hello, welcome to Guess a Number A.I. What is your name? ")
    play(name)
    playing = play_again(name)

show_credits()
