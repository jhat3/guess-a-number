import random

#config
high=100
low=1
limit=10

#start game
rand = random.randrange(low,high)
print("I'm thinking of a number from " + str(low) + "to " + str(high) + ".");

guess = -1
tries = 0

#helper functions
def get_guess():
    while True:
        g=input("Take a guess: ")

        if g.isnumeric():
            g=int(g)
            return g
        else:
            print("You must enter a number")

#play the game
while guess != rand and tries < limit:
    guess = get_guess()
    
    guess = input("Take a guess: ")
    guess = int(guess)
    
    if guess < rand:
        print("You guessed too low.")
    elif guess > rand:
        print("You guessed too high.")

    tries += 1

#tell player outcome
if guess == rand:
    print("You win!")

else:
    print("You lose. I was thinking of " +str(rand)+ ".")
