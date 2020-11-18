import random

print("Hi! Welcome to the game. What is your name?")
name = input()
print("Well, " + name + " I am thinking of a number between 1 and 20..")
secretNumber = random.randint(1, 20)

##for loop - player has 6 tries
for guessesTaken in range(1, 7):
    print("Take another guess..")
    playerGuess = int(input())

    if playerGuess < secretNumber:
        print("Nope! Your guess is too low")
    elif playerGuess > secretNumber:
        print("Nope Your guess is too high")
    else:
        break #this condition is for the correct guess

#if player guesses correctly
if playerGuess == secretNumber:
    print("Good job! You took " + str(guessesTaken) + " guesses to win!")
else:
    print("Nope. The number I was thinking of is " + str(secretNumber))

