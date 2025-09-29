import random

# Ask the user how many dice to roll
num_dice = int(input("How many dice would you like to roll? "))

total = 0

# Roll the dice using a for loop
for _ in range(num_dice):
    roll = random.randint(1, 6)  # Simulate a die (1-6)
    total += roll

print(f"The total sum of the dice is: {total}")
