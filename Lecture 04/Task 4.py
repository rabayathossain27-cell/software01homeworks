import random

# Computer picks a random number between 1 and 10
secret_number = random.randint(1, 10)

print("I'm thinking of a number between 1 and 10.")
print("Try to guess it!")

while True:
    try:
        guess = int(input("Enter your guess: "))

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print("Correct! You guessed the number!")
            break  # end the game
    except ValueError:
        print("Please enter a valid number.")
