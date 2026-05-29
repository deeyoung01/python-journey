#Mini Calculator Using Functions
def add(a,b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by Zero"
    return a / b
#Get input from the user
num1 = float(input("Enter First Number: "))
num2 = float(input("Enter Second Number: "))
print("\n Choose Operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("\nEnter choice (1/2/3/4): ")

#Call the correct funtion based on choice
if choice == "1":
    result = add(num1, num2)
    print(f"\nResult: {num1} + {num2} = {result}")
elif choice == "2":
        result = subtract(num1, num2)
        print(f"\nResult: {num1} - {num2} = {result}")
elif choice == "3":
        result = multiply(num1, num2)
        print(f"\nResult: {num1} * {num2} = {result}")
elif choice == "4":
        result = divide(num1, num2)
        print(f"\nResult: {num1} / {num2} = {result}")
else:
    print("Invalid Choice!")