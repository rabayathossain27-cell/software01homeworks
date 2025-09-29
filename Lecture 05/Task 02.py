numbers = []

while True:
    user_input = input("Enter a number (or press Enter to quit): ")
    if user_input == "":  # Empty string → stop
        break
    try:
        number = float(user_input)  # Convert to number (supports decimals)
        numbers.append(number)
    except ValueError:
        print("Please enter a valid number.")

# Sort numbers in descending order
numbers.sort(reverse=True)

# Get the top five numbers
top_five = numbers[:5]

print("The five greatest numbers are:", top_five)
