# Program to find smallest and largest numbers from user input

numbers = []

while True:
    user_input = input("Enter a number (leave blank to stop): ")

    if user_input == "":  # blank input stops the loop
        break

    try:
        number = float(user_input)
        numbers.append(number)
    except ValueError:
        print("Invalid input. Please enter a number.")

if numbers:
    print(f"Smallest number: {min(numbers)}")
    print(f"Largest number: {max(numbers)}")
else:
    print("No numbers were entered.")
