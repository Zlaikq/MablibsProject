import random

choice = input("Which game would you like to play? Enter user guess, computer guess, or q to quit: ")

while choice not in ['user guess', 'computer guess', 'q']:
    print("Please enter a valid input.")
    choice = input("Which game would you like to play? Enter user guess, computer guess, or q to quit: ")

if choice == "user guess":
    numberToGuess = random.randint(0, 100)
    userGuess = int(input("Guess a number between 0-100: "))
    while userGuess != numberToGuess:
        while userGuess > numberToGuess:
            userGuess = int(input("Number is too high, enter a lower value: "))
        while userGuess < numberToGuess:
            userGuess = int(input("Number is too low, enter a higher value: "))
    print("Congratulations! You guessed the number!")
    
elif choice == "computer guess":
    lowNum = 0
    highNum = 100

    humanNumber = int(input("Enter a number between 0-100 for the computer to guess: "))

    while humanNumber < lowNum or humanNumber > highNum:
        humanNumber = int(input("Please enter a valid number between 0-100: "))

    computerGuess = random.randint(lowNum, highNum)

    while computerGuess != humanNumber:
        while computerGuess > humanNumber:
            print("Computer guessed " + str(computerGuess) + ", too high.")
            highNum = computerGuess 
            computerGuess = random.randint(lowNum, computerGuess) 
            

        while computerGuess < humanNumber:
            print("Computer guessed " + str(computerGuess) + ", too low.")
            lowNum = computerGuess 
            computerGuess = random.randint(computerGuess, highNum)

    if computerGuess == humanNumber:
        print("Computer guessed the number!: " + str(computerGuess) + ".")

elif choice == "q":
    print("Goodbye!")
    exit()

