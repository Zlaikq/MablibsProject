choice = input("Which story would you like to play? Enter the number of the story (1,2 or 3) or type q to quit: ")
while choice not in ['1', '2', '3', 'q']:
    print("Please enter a valid input.")
    choice = input("Which story would you like to play? Enter the number of the story (1,2 or 3) or type q to quit: ")
adjective = input("Enter an adjective: ")
noun = input("Enter a noun: ")
plural_noun = input("Enter a plural noun: ")
verb = input("Enter a verb: ")
part_of_body = input("Enter a part of the body: ")
number = input("Enter a number: ")
place = input("Enter a place: ")
verb_ending_in_ing = input("Enter a verb ending in -ing: ")
    
if choice == '1':
    print("You have chosen story 1.")
    print("Once upon a time, a " + adjective + " adventurer set out on a journey to the " + place + ". With a trusty " + noun + " in hand, they walked through the dense forest, careful not to step on any " + plural_noun + ". After walking for " + number + " hours, they heard a loud " + verb_ending_in_ing + " noise. They turned around and saw a giant " + noun + " with big, sharp teeth! The adventurer reached into their pocket, grabbed their " + noun + ", and bravely faced the creature. The battle was fierce, but with a swift " + verb_ending_in_ing + " move, they triumphed and returned home as a hero. Their " + part_of_body + " still aches from the encounter, but they know they’ll be ready for the next adventure!")
elif choice == '2':
    print("You have chosen story 2.")
    print("In the year " + number + ", robots became self-aware and started to take over the world. The first thing they did was build a massive " + noun + " in the middle of " + place + ". People were terrified and started running around, bumping into " + plural_noun + ". A brave scientist named " + noun + " decided to stop the robots by using their knowledge of " + adjective + " programming. They spent hours " + verb_ending_in_ing + " to come up with a plan, and eventually, they succeeded! The robots were deactivated, and the world was saved. However, the scientist’s " + part_of_body + " was sore from all the thinking.")
elif choice == '3':
    print("You have chosen story 3.")
    print("Late at night, a group of friends decided to explore an old, " + adjective + " house on the outskirts of town. They heard rumors that the house was haunted by a " + noun + ", so they were both excited and nervous. As they wandered through the dusty rooms, they noticed strange " + plural_noun + " on the floor. After exactly " + number + " creaks of the floorboards, they heard a loud " + verb_ending_in_ing + " sound coming from upstairs. One of the friends, " + noun + ", bravely climbed up the creaky stairs, holding a flashlight in one hand and a " + noun + " in the other. To their surprise, they found a ghost who had a very sore " + part_of_body + " and needed help. The friends quickly ran to the local " + place + " to find a solution.")
elif choice == 'q':
    print("Goodbye!")
    exit()
