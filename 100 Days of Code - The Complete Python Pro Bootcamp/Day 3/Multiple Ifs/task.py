print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? \n"))
age = int(input("What is your age? \n"))
price =0
if height >= 120:
    print("You can ride the rollercoaster")
    if age >= 18:
        price = 12
    elif age >= 12:
        price = 7
    else:
        price = 5
    photos=input("Do you want photos(y / n)? \n")
    if photos == "y":
        print("Total bill is: $", price+5)
    else:
        print("Total bill is: $", price)
else:
    print("Sorry you have to grow taller before you can ride.")
