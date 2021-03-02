#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
password = ''
alphabet = letters
for letter in range(nr_letters):
  password += random.choice(letters)
for symb in range(nr_symbols):
  password += random.choice(symbols)
for num in range(nr_numbers):
  password += random.choice(numbers)
print("Your password is: " + password)


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password2 = ''
alphabet2 = letters
for letter in range(nr_letters):
  password2 += random.choice(letters)
for symb in range(nr_symbols):
  password2 += random.choice(symbols)
for num in range(nr_numbers):
  password2 += random.choice(numbers)
pwd = list(password2)
random.shuffle(pwd)
stronger = "".join(pwd)

print("Your stronger password is: " + stronger)

#Another way to do the Hard Level, without .join()

password2 = ''
alphabet2 = letters
for letter in range(nr_letters):
  password2 += random.choice(letters)
for symb in range(nr_symbols):
  password2 += random.choice(symbols)
for num in range(nr_numbers):
  password2 += random.choice(numbers)
print(password2)
pwd = list(password2)
random.shuffle(pwd)
print(pwd)

new_pass = ""
for char in password2:
  new_pass += char

print(f"Your new password is: {new_pass}")
