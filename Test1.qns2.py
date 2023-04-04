
color1 = input("Enter the first primary color: ").lower()
color2 = input("Enter the second primary color: ").lower()

RED = "red"
BLUE = "blue"
YELLOW = "yellow"


if color1 not in [RED, BLUE, YELLOW]:
    print("Error: Invalid Color1")
elif color2 not in [RED, BLUE, YELLOW]:
    print("Error: Invalid Color2")
elif color1 == color2:
    print("Error: The two colors you entered are same")
else:
    if color1 == RED:
        if color2 == BLUE:
            print("PURPLE")
        elif color2 == YELLOW:
            print("ORANGE")
    elif color1 == BLUE:
        if color2 == RED:
            print("PURPLE")
        elif color2 == YELLOW:
            print("GREEN")
    elif color1 == YELLOW:
        if color2 == RED:
            print("ORANGE")
        elif color2 == BLUE:
            print("GREEN")