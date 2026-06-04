#Loop 
    #Ask: rool the dice?
    #if uswer enter y
    #Generate two random numbers
    #print them
    #if user enters n
    #print thank you message
    #Terminate
    #Else
    #print invalid choice!
import random

while True:
    user = input("Roll the dice? (y/n): ")
    if user == "y":
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        print("=" * 35)
        print(f'Rolled Out: ({die1},{die2})')
        print(f'Good Job \N{fire}')
        print("=" * 35)
    elif user == "n":
        print(f'Thanks for playing!')
        break
    else:
        print(f'Invalid Choice')