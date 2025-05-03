import random


top_secret = random.randint(1, 100)

print("Guess a number between 1 and 100.")

while True:
    try:
        guess = int(input("Enter your guess: "))
        if guess < top_secret:
            print("Too low... Try again")
        elif guess > top_secret:
            print("Too high... Try again")
        else:
            print("Congrats! You guessed the number")
            break
    except ValueError:
        print("Enter a valid number NOW !!")