choice = input("Which story would you like to play? Enter the number of the story (1,2 or 3) or type q to quit: ")
while input not in ['1', '2', '3', 'q']:
    print("Please enter a valid input.")
    choice = input("Which story would you like to play? Enter the number of the story (1,2 or 3) or type q to quit: ")
    
if choice == '1':
    print("You have chosen story 1.")
elif choice == '2':
    print("You have chosen story 2.")
elif choice == '3':
    print("You have chosen story 3.")
elif choice == 'q':
    print("Goodbye!")
    exit()
