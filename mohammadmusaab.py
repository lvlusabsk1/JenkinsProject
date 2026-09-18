print ("Hello from Mohammad Musaabs Jenkins CI/CD pipeline!")
print ("This app was built, containerized, and pushed to DockerHub automatically")
print("Below is a sample project from geekforgeeks that runs a simple calculator with basic operations like addition, subtraction, multiplication and division")


def add(n1, n2):
    return n1 + n2
 
 
def sub(n1, n2):
    return n1 - n2
 
 
def mul(n1, n2):
    return n1 * n2
 
 
def div(n1, n2):
    if n2 == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return n1 / n2
 
 
def get_number(prompt):
    """Keep asking until the user provides a valid number."""
    while True:
        value = input(prompt)
        if value.strip() == "":
            print("Input cannot be empty. Please enter a number.")
            continue
        try:
            return float(value)
        except ValueError:
            print("That's not a valid number. Please try again.")
 
 
def get_operation():
    """Keep asking until the user picks a valid operation (1-4)."""
    while True:
        value = input("Select operation (1-4): ")
        if value.strip() == "":
            print("Input cannot be empty. Please enter a number between 1 and 4.")
            continue
        try:
            choice = int(value)
        except ValueError:
            print("That's not a valid whole number. Please enter 1, 2, 3, or 4.")
            continue
        if choice not in (1, 2, 3, 4):
            print("Please choose a number between 1 and 4.")
            continue
        return choice
 
 
print("Please select operation -\n"
      "1. Add\n"
      "2. Subtract\n"
      "3. Multiply\n"
      "4. Divide\n")
 
sel = get_operation()
 
n1 = get_number("Enter first number: ")
n2 = get_number("Enter second number: ")
 
try:
    if sel == 1:
        print(n1, "+", n2, "=", add(n1, n2))
    elif sel == 2:
        print(n1, "-", n2, "=", sub(n1, n2))
    elif sel == 3:
        print(n1, "*", n2, "=", mul(n1, n2))
    elif sel == 4:
        print(n1, "/", n2, "=", div(n1, n2))
except ZeroDivisionError as e:
    print(f"Error: {e}")