# Calculator program
#Operation to perform Addition
def add(a, b):
    return a + b

#Operation to perform subtraction
def sub(a, b):
    return a - b

#Operation to perform multiplication
def multiply(a, b):
    return a * b

#Operation to perform division
def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error! Divided by zero."

# Main program
def calculator():
    print("Simple Calculator")
    print("Select operation:")
    print("1. Add")
    print("2. Sub")
    print("3. Multiply")
    print("4. Divide")
    
    # Taking input from the user
    choice = input("Enter choice (1/2/3/4): ")
    
    if choice in ['1', '2', '3', '4']:
        # Input numbers
        n1 = float(input("Enter first number: "))
        n2 = float(input("Enter second number: "))
        
        # Perform the calculation based on the user's choice
        if choice == '1':
            print(f"{n1} + {n2} = {add(n1, n2)}")
        elif choice == '2':
            print(f"{n1} - {n2} = {subtract(n1, n2)}")
        elif choice == '3':
            print(f"{n1} * {n2} = {multiply(n1, n2)}")
        elif choice == '4':
            print(f"{n1} / {n2} = {divide(n1, n2)}")
    else:
        print("Please enter a valid input.")

# Run the calculator
calculator()
