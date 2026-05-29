'''
first_name = 'Samuel'
last_name = 'Ilori'
full_name = first_name + ' ' + last_name
print(full_name)

username = 'tobi'
password = 'padam'
long_sting = '''
    #WOW
    #O O
     #-
'''
print(long_sting)
print('hello'+' Ilori')
#escape sequence
weather = "\t It\'s \"kind of \"sunny \n hope you have a good day!"
print(weather)
#Formatted strings
age = 10
print(f'hi {name}! are you a {age} years old boy')
#a project exec
birth_year = input('what year were you born?')
age = 2026 - int(birth_year)
print(f'your age is: {age} years old')
#password checker
username = input('what is your username? ')
password = input('what is your password? ')
password_length = len(password)
hidden_password = '*' * password_length
print(f'{username} your password {hidden_password} is {password_length} letters long')
#adding a list
basket = ['a','b','c','d','e']
new_list = basket.extend([100])
basket.reverse()
print(basket)
print('d' in basket)
print('I' in 'hi my name is ilori')
print(basket.count('d'))
#let's create a car that detect
is_old = False
is_licenced = True

if is_old:
    print('you are old enough to drive')
elif is_licenced:
    print('you can a drive now')
else:
    print('you are not of age!')

    print('checheck')
#determine a user is your friend
is_friend = False
can_message = "Message allowed" if is_friend else "not allowed to message"
print(can_message)
print(410 >= 5)
#Create a wizard Game
is_magician = True
is_expert = False

if is_magician and is_expert:
    #print("you are a master Magician")
elif is_magician and not is_expert:
    print("At least you're getting there")
else:
    print("you need magic powers")
#Build a counter
my_list = [1,2,3,4,5,6,7,8,9,10]
counter = 0
for item in my_list:
    counter = counter + item
print(counter)
Return 
def sum(num1, num2):
    def another_func(n1, n2):
        return n1 + n2
    return another_func(num1, num2) 
total = sum(10, 20)
print(total)
# Exercise Functions
def highest_even(li):
    evens = []
    for item in li:
        if item % 2 == 0:
            evens.append(item)
        return max(evens)

print(highest_even([10,2,3,4,8,11]))

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

for number in range(5):
    print(number)
for letter in "Python":
    print(letter)
foods = ["pizza", "sushi", "amala"]
for index, food in enumerate(foods):
    print(f"{index}: {food}")
#while loops
count = 5
while count > 0:
    print(count)
    count -= 1
#user input validation'''
while True:
    username = input("Enter username: ")
    password = input("Enter Password: ")
    if username == "David" and password == "David123":
        print("Access granted!")
        break
    else:
        print("Incorrect username or password. Try again")
        
for i in range(1, 13):
    print(f"7 x {i} = {7 * i}")
for a in range(1, 13):
    print(f"2 x {a} = {2 * a}")
#Find the Largest Number
numbers = [3,7,2,9,1,5,20,32,50,100,]
largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num
print(f"The Largest Number is: {largest}")
#How Many Rounds Until Broke
import random
money = 100
rounds = 0

while money > 0:
    loss = random.randint(1, 40)
    money -= loss
    rounds += 1
    print(f"Round {rounds}: Lost ${loss} - Remaining: ${max(money, 0)}")
    print("-" * 35)
print(f"\nBroke after {rounds} rounds!")

#sum if a list
#numbers = [1,20,30,40,50]
#total = 0
#for i in numbers:
#    total += i

#    print(f"Total: {total}")
word = "programming"
vowels = "aeiou"
count = 0
 #    if letter in vowels:
 #       count += 1
#print(f"vowels in '{word}': {count}")
for i in range(2,21,2):
    print(i, end=" ")
print("\N{bomb}" )
print("\N{fire}" )
print("\N{fish}" )
print("\N{whale}" ) 
print("\N{trophy}" )
print("\N{ship}" )
print("-"* 35)
#gon
total = 0
for i in range(1, 101):
    total += 1
print(f"Sum: {total}")

