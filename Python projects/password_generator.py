import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '@', '#', '$','%', '&', '*', '<', '>', '(', ')']

print("\n---------- Welcome TO password Generator! ----------\n")
print("\n -------------- Made by Manas Chavan ---------------")

n_letters = int(input("Enter letters you want in the password : "))
n_numbers = int(input("Enter numbers you want in the password : "))
n_symbols = int(input("Enter symbols you want in the password : "))

password = []

for i in range(1, n_letters+1):
    chars = random.choice(letters)      # Randomizing the letters list
    password += chars                
    
for i in range(1, n_numbers+1):
    chars = random.choice(numbers)      # Randomizing the numbers list
    password += chars

for i in range(1, n_symbols+1):
    chars = random.choice(symbols)      # Randomizing the symbols list
    password += chars 

random.shuffle(password)    # using shuffle to shuffle the list

final_password = ""     # Empty string to store shuffled password

for chars in password:
    final_password += chars         # Adding the shuffles password to string from the list 

print(f"\n Password is generated : {final_password}")

