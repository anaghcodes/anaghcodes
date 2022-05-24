
def calculator(num1, num2, op):
    sol = 0
    invalid = 0
    if op == "+":
        sol = num1 + num2
    elif op == "-":
        sol = num1 - num2
    elif op == "*":
        sol = num1 * num2
    elif op == "x":
        sol = num1 * num2
    elif op == "÷":
        sol = num1 / num2
    elif op == "/":
        sol = num1 / num2
    else:
        invalid = 1
        print("Invalid Operator!")
    if invalid == 1:
        print(" ")
    else:
        print(float(sol))
        print("Made by Anagh")
        print(" ")

try_again = input("Enter 'C' to use the calculator: ")
while try_again == "C" or "c":
        calculator(float(input("Enter the first number: ")), (float(input("Enter the second number: "))),
               (input("Enter the sign of the operation that you want to do: ")))
        continue

