#validation of names
middlename = input("Enter Middlename: ")
lastname = input("Enter Lastname: ")

while not middlename or not lastname:
    print("Please fill up both name(s)")
    middlename = input("Enter Middlename: ")
    lastname = input("Enter Lastname: ")
print(f"Welcome Mr.{middlename} {lastname} \N{fire}")
