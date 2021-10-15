import random 

# Function that shuffles characters of string

def shuffle(string):
    tempList = list(string)
    random.shuffle(tempList)
    return "".join(tempList)

# Variables 

uppercaseLetter1 = chr(random.randint(65,90)) # Generates random uppercase letter (ASCII CODE)
uppercaseLetter2 = chr(random.randint(65,90)) # Generates random uppercase letter (ASCII CODE)

lowercaseLetter1 = chr(random.randint(97,122)) # Generates random lowercase letter (ASCII CODE)
lowercaseLetter2 = chr(random.randint(97,122)) # Generates random lowercase letter (ASCII CODE)

number1 = chr(random.randint(48, 57)) # Generates random number (ASCII CODE)
number2 = chr(random.randint(48, 57)) # Generates random number (ASCII CODE)

symbol1 = chr(random.randint(33, 47)) # Generates random symbol (ASCII CODE)
symbol2 = chr(random.randint(33, 47)) # Generates random symbol (ASCII CODE)

# Generates password and shuffles

password = (uppercaseLetter1 + uppercaseLetter2 + lowercaseLetter1 + lowercaseLetter2 + number1 + number2 + symbol1 + symbol2)

password = shuffle(password)

# Output

print(password)