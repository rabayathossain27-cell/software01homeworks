# Minimum legal length for a zander in cm
LEGAL_SIZE = 42

# Ask the user for the fish length
length = int(input("Enter the length of your zander in centimeters : "))

# Check if the fish meets the size requirement
if length < LEGAL_SIZE :
    short = LEGAL_SIZE - length
    print(f"The zander is too small. please release it back into the lake")
    print(f"It is {short} cm shorter than the legal limit.")
else :
    print("The zander meets the size requirement. You can keep it.")