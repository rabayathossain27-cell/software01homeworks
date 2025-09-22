# Program to convert inches to centimeters until user enters a negative value

while True:
    inches = float(input("Enter length in inches (negative value to stop): "))

    if inches < 0:
        print("Program stopped.")
        break  # exit the loop

    centimeters = inches * 2.54
    print(f"{inches} inches = {centimeters:.2f} cm")

