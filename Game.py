import random
import math

#Intro for user
print("-------------------------------------\n")
print("Welcome to the Numbers Guessing Game\n")
print("-------------------------------------\n")
print("You can decide the guessing range!\n")

#Receive lower bound input from user
lower = input("Enter the lower bound: ")
while (lower.isdigit() == False):
    print("Please enter a valid integer.\n")
    lower = input("Enter the lower bound: ")
#Receive upper bound input from user
upper = input("Enter the upper bound: ")
while (upper.isdigit() == False):
    print("Please enter a valid integer.\n")
    upper = input("Enter the upper bound: ")
lower = int(lower)
upper = int(upper)
#calculate minimun guesses required to guess the random number
#This can be achieved by the user by guessing half of the range, repeatedly until the random number is guessed
minGuess = round(math.log(upper - lower + 1, 2))

#Counter for number of guesses the user has used
guessCounter = 1

#Generates random integer within lower and upper range(including)
ranNum = random.randint(lower, upper)

#Display chances to user
print("\nYou have " + str(minGuess) + " chances to guess correctly.\n")

#Receive first guess from user
guess = input("Enter guess #" + str(guessCounter) + ": ")
while (guess.isdigit() == False):
    print("Please enter a valid integer.\n")
    guess = input("Enter guess #" + str(guessCounter) + ": ")
#Loops until guess == random number or until the user is out of chances
while(int(guess) != ranNum and guessCounter < minGuess):
    #Notify user that their guess was too high
    if (int(guess) > ranNum):
        print("Your guess was too high!")
    #Notify user tha their guess was too low
    else:
        print("Your guess was too low!")
    #Display number of remaining guesses to user
    print("\nYou have " + str(minGuess - guessCounter) + " guesses remaining.")

    #Add 1 to guessCounter
    guessCounter += 1

    #Receive new guess from user
    guess = input("\nEnter guess #" + str(guessCounter) + ": ")
    while (guess.isdigit() == False):
        print("Please enter a valid integer.\n")
        guess = input("Enter guess #" + str(guessCounter) + ": ")
#If guess was correct, display output
if (guess == ranNum):
    print("\nGreat job! You guessed the number in " + str(guessCounter) + " attempt(s)!")

#If guess was incorrect, display output and show random number
else:
    print("\nYou ran out of chances! The random number was " + str(ranNum) + ". \n\nBetter luck next time!")
