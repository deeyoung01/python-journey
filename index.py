#Keep asking for a name until the user type something
surname = input("Enter your Surname: ")
firstname = input("Enter your Firstname: ")

while not surname or not firstname:
    print(f"Please provide Proper name(s)")
    surname = input("Enter your Surname: ")
    firstname = input("Enter your Firstname: ")


print(f"Welcome onboard, Mr {surname} {firstname}! \N{fire}")