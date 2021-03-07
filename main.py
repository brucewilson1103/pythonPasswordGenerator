import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to Bruce's Python Password Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols should your password have?\n"))
nr_numbers = int(input(f"How many numbers should your password have?\n"))

password = []

for item in range(1, nr_letters + 1):
  password.append(random.choice(letters))

for item in range(1, nr_symbols + 1):
  password += random.choice(symbols)

for item in range(1, nr_numbers + 1):
  password += random.choice(numbers)

print(password)
random.shuffle(password)
print(password)

passwordFinal = ""
for item in password:
  passwordFinal += item

print(f"Your suggested Python password is: {passwordFinal}")