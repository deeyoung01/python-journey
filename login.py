#simple Login System
username = input("Enter Username: ")
password = input("Enter Password: ")
counters = 0
max_counters = 3
while counters < max_counters:
        print(f"Incorrect username or password")
        username = input("Enter Username: ")
        password = input("Enter Password: ")
        counters += 1
        if username == "admin" and password == "1234":
            print(f"Login Succesful \U00002705")
            break

      