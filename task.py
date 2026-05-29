#Name validation program
surname = input("Enter Surname: ")
firstname = input("Enter Firstname: ")

while not surname or not firstname:
    print("Please enter both name(s)")
    surname = input("Enter Surname: ")
    firstname = input("Enter Firstname: ")
print(f"Welcome {firstname} {surname}")
