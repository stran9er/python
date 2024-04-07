import random as rnd
print("Simple password generator, you may check the strenght of the final return over at\n"
      "https://www.security.org/how-secure-is-my-password/\n"
      "This is for educational purposes only")

# A password must have letters, numbers, and symbols in order to be a strong password.
letters = ['a', 'b','c', 'd', 'e', 'f', 'g', 'h',
           'i', 'j', 'k', 'l', 'm', 'n', 'o',
           'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
           'I', 'J', 'K', 'L', 'M', 'N', 'O',
           'P', 'Q', 'R', 'S', 'T', 'U', 'V',
           'W', 'X', 'Y', 'Z',
           ]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '^', '&', '*', '@', '(', ')', ',', '.', '+']

# Asks the user how many letters, numbers, and symbols the password must have.
num_letters = int(input("How many letters would you like your password to have?  "))
num_numbers = int(input("How many numbers would you like your password to have?  "))
num_symbols = int(input("How many symbols would you like your password to have?  "))

pass_word = ""          # Will be used at the end to pass the list as string.
password_list = []      # Will hold the values based on user entry.

# For the amount of letters the user wants, append your list with a random letter.
for char in range (1, num_letters + 1):
    password_list.append(rnd.choice(letters))

# For the amount of numbers the user wants, append your list with a random number.
for char in range (1, num_numbers +1):
    password_list.append(rnd.choice(numbers))

# For the amount of symbols the user wants, append your list with a random symbol.
for char in range (1, num_symbols +1):
    password_list.append(rnd.choice(symbols))

# Let's shuffle the list contents. 
rnd.shuffle(password_list)

# For each item in the password_list, after shuffle add to the the string.
for i in password_list:
    pass_word += i

print(f"Your new password is:  {pass_word}")
