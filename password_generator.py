import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to password generator.")
nr_letters = int(input("How many letters: "))
nr_numbers = int(input("How many numbers: "))
nr_symbols = int(input("How many symbols: "))

pw = ""

for num_letter in range(0, nr_letters):
  pw += random.choice(letters)

for num_number in range(0, nr_numbers):
  pw += random.choice(numbers)

for num_symbol in range(0, nr_symbols):
  pw += random.choice(symbols)

shuffled_pw = ''.join(random.sample(pw, len(pw)))

print(shuffled_pw)

