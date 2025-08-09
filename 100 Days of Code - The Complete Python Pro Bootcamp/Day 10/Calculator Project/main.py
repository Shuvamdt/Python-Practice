import art
def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1-n2
def multiply(n1, n2):
    return n1*n2
def divide(n1, n2):
    return n1/n2
operations={
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}
def calculator():
    print(art.logo)
    choice = 'y'
    a = float(input("What's the first number?:  "))
    while choice == 'y':
        for key in operations:
            print(key)
        opr = input("Pick an operation:  ")
        b = float(input("What's the next number?:  "))
        result = operations[opr](a, b)
        print(f"{a} {opr} {b} = {result}")
        choice = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
        if choice == 'y':
            a=result
        else:
            print("\n"*20)
            calculator()
calculator()