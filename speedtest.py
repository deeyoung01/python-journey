while True:
    try:
        users = input("Enter your Age: ").lower()
        age = 2026 - int(users)
        print(f"You are {age}years Old") 
        break
    except ValueError:
        print("Please enter a valid age.")