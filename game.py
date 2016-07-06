# Put your code here
#Greet player
import random
print "Welcome to the guessing game! What is your name? "
name = raw_input("Enter your name: ")
print "Welcome %s, I'm thinking of a number 1 - 100, try to guess it!" % name
answer = random.randint(0, 100)
guess = int(raw_input("guessed number"))

while True:
    if guess == answer:
        print "Congratulations!"
        break
    elif guess >= answer:
        print "Too high, guess lower."
        guess = int(raw_input("New Guess: "))
    else:
        print "Too low, guess higher."
        guess = int(raw_input("New Guess: "))