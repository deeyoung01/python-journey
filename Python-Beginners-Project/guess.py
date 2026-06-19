import random

while True:
    try:
        user = int(input('Guess a number: '))
        number = random.randint(1, 100)
        if not user:
            print(f'Error')
        elif user == number:
            print(f'Correct number guess')
        elif user < number:
            print(f'Too Low')
        elif number > user:
            print(f'Too High')
        else:
            print(f'Well done!')
            break
    except ValueError:
        print('Please enter valid number')
