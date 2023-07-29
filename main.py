import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def valid_int_input(user_input):
  try:
      user_input = int(user_input)
  except ValueError:
      print("That is not a number. Try again.")
      return False

  return True

def positive_number_input(user_input):
  if user_input < 0:
    print("You cannot enter a negative number. Try again.")
    return False
  else:
    return True

print("Welcome to the Password Generator!")
valid_input = False
while not valid_input:
  nr_letters = input("How many letters would you like in your password? ")
  valid_input = valid_int_input(nr_letters)
  if valid_input == True:
    nr_letters = int(nr_letters)
    valid_input = positive_number_input(nr_letters)

valid_input = False
while not valid_input:
  nr_symbols = input(f"How many symbols would you like? ")
  valid_input = valid_int_input(nr_symbols)
  if valid_input == True:
    nr_symbols = int(nr_symbols)
    valid_input = positive_number_input(nr_symbols)

valid_input = False
while not valid_input:
  nr_numbers = input(f"How many numbers would you like? ")
  valid_input = valid_int_input(nr_numbers)
  if valid_input == True:
    nr_numbers = int(nr_numbers)
    valid_input = positive_number_input(nr_numbers)

password_characters = []
for char in range(0, nr_letters):
  password_characters.append(random.choice(letters))

for char in range(0, nr_symbols):
  password_characters.append(random.choice(symbols))

for char in range(0, nr_numbers):
  password_characters.append(random.choice(numbers))

password_length = nr_letters + nr_symbols + nr_numbers
randomized_password = ""
for x in range(0, password_length):
  remaining_char_length = password_length - x
  random_char_position = random.randint(0, remaining_char_length-1)
  random_char = password_characters[random_char_position]
  randomized_password = randomized_password + random_char
  password_characters.pop(random_char_position)

print(f"Here is your random password: {randomized_password}")


