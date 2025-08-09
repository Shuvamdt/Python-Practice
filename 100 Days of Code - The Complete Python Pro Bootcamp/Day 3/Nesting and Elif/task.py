print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? \n"))
age = int(input("What is your age? \n"))

if height >= 120:
    print("You can ride the rollercoaster")
    if age >= 18:
        print("Price : $12")
    elif age >= 12:
        print("Price : $7")
    else:
        print("Price: $5")
else:
    print("Sorry you have to grow taller before you can ride.")
