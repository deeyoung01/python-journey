#write a nuber guessing game
import random

secret = random.randint(1, 100)
attempts = 0
max_attempts = 3
while attempts < max_attempts:
    guess = int(input("Guess a number (1-100): "))
    attempts += 1
    if guess == secret:
        print(f"(\u2764\U00002705 Correct! You got it in {attempts}) attempts!")
        break
    diiference = abs(secret - guess)
    hints = [
        (5, "\u2764\uFE0F Boiling! Extremely close!"),
        (10, "Very Warm"),
        (20, "\U0001F525 Warm"),
        (40, "\u2764 Cold"),
    ]
    for limit, message in hints:
        if diiference <= limit:
            print(message)
            break
    else:
        print("\U0001F40D Freezing! way off!")
        remaining = max_attempts - attempts
        print("-" * 40)
        print(f" {'Higher' if guess < secret else 'Lower'}! {remaining} attempts left.\n")
else:
        print(f"\N{cross mark} Game over! The number was {secret}.")