import random
words = ("tecnology","book","chess","bear","python","computer","terminator","machine","global","background","orange","future","warrior")

gameRange = 0
done = False
guesses = []
letter = " "

user = input("What's your user name: ")
print(f"Welcome {user}!")

choice = random.choice(words)


while not done:
    for letter in choice:
        if letter in guesses:
            print(letter, end=" ")
        else:
            print("_", end=" ") 
    print("")
    guess = input("Guess a letter: ")
    guesses.append(guess)
    if guess not in choice:
        gameRange = gameRange + 1
        print(f"Bad choice, '{guess}' didn't in word!")
        if gameRange == 6:
            print(f"You lose, true answer was {choice}.")
            quit()
    done = True
    for letter in choice:
        if letter not in guesses:
            done = False
if done == True:
    print(f"Congratulations, you found the '{choice}'!")
else:
    print(f"You lose, true answer was {choice}.")