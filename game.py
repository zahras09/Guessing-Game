# Put your code here.
import random

#Greet player
print "Welcome to the guessing game! What is your name? "
#User inputs name, save as name
name = raw_input("Enter your name: ")
print "Welcome %s, I'm thinking of a number 1 - 100, try to guess it!" % name
#Randint is a function that pulls a random number between 2 bounds from random module
answer = random.randint(0, 100)



#User inputs answer, transform string into integer
#guess = int(raw_input("Guessed number: "))

#While loops sets a condidtion that won't stop until guess equals answer
while True:
    #Try and except functions handle cases where guesses are not numbers
    try:
        guess = int(raw_input("Guessed number: "))
    except ValueError:
        print "Please enter an integer..."
        continue
        #guess = int(raw_input("Guessed number: "))

    #Bounds the users' guess between 0 and 100
    if guess < 0 or guess > 100:
        print "Learn how to count! Enter a new number between 0 - 100"
        guess = int(raw_input("Guessed number: "))

    #Conditional specifying if guess = answer to exit the loop
    elif guess == answer:
        print "Congratulations!"
        #Breaks infinite loop
        break

    elif guess > answer:
        print "Too high, guess lower."
        guess = int(raw_input("New Guess: "))

    elif guess < answer:
        print "Too low, guess higher."
        guess = int(raw_input("New Guess: "))
