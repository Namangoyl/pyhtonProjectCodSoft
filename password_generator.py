import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '"', '#', '$', '%', '&']

print("welcome to the password generator!")

nr_letter = int(input("how many letter would you like in your password: \n "))

nr_symbol = int(input(f"how many symbol would you like: \n"))

nr_number = int(input(f"how many number would you like: \n"))

password = ""

for char in range(1, nr_letter + 1):
    
    # 1 - 4
    #random_char=random.choice(letter)
    #password += random_char 
    
    password += random.choice(letters)
    
for symbol in range(1, nr_symbol + 1):
    
    password += random.choice(symbols)
    
for numeber in range(1, nr_number + 1):
    
    password += random.choice(numbers)
    
print(password)    
