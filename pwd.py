#password Generator
import random
import string

def generate_password(length=12, use_upper=True, use_digits=True, use_symbols=True):
    chars = string.ascii_lowercase
    if use_upper: chars += string.ascii_uppercase
    if use_digits: chars += string.digits
    if use_symbols: chars += "!@#$%^7*()_+-=[]{}|"

    password =""
    for _ in range(length):
        password += random.choice(chars)
    return password

def check_strength(password):
    score = 0
    if len(password) >= 8:      score += 1
    if len(password) >= 12:     score += 1
    if any(c.isupper() for c in password): score += 1
    if any(c.isdigit() for c in password): score += 1
    if any(c in "!@#$%^&*()" for c in password): score += 1

    levels = {5: "Very Strong", 4: "Strong", 3: "Medium", 2: "Weak", 1: "Very Weak"}
    return levels.get(score, "Very Weak")
    
print("PASSWORD GENERATOR")
print("=" * 35)
length = int(input("Password Length (8-32): "))
upper = input("Include uppercase? (y/n): ").lower() == "y"
digits = input("Include numbers? (y/n): ").lower() == "y"
symbols = input("Include symbols? (y/n): ").lower() == "y"

print("Generated Passwords:")
print("-" * 35)
for i in range(5):
    pwd = generate_password(length, upper, digits, symbols)
    strength = check_strength(pwd)
    print(f" {i+1}, {pwd}   {strength}")