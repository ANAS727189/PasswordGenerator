import random
import string

letters = list(string.ascii_letters) 
numbers = list(string.digits) 
symbols = list(string.punctuation) 

print("Welcome to The world of password generation !!")
print("Generate passwords like a pro.")

n_letters = int(input("How many letters do you want in your password? "))
n_numbers = int(input("How many numbers do you want in your password? "))
n_symbols = int(input("How many symbols do you want in your password? "))

password_list = []

for i in range(n_letters):
    password_list.append(random.choice(letters))

for i in range(n_numbers):
    password_list.append(random.choice(numbers))

for i in range(n_symbols):
    password_list.append(random.choice(symbols))

random.shuffle(password_list)
password = " "
for i in password_list:
    password += i

print(f"Generated Password: {password}")
