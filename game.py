import random
computerChoice = random.randint(1,6)
userChoice = input("Choose a number from 1 to 6 : ");

if userChoice == computerChoice:
    print("You guessed correctly!");
else:
    print("You guessed wrong.");
