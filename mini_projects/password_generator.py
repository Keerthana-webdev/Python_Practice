import random
import string

def generate_password(length):
    chars = string.ascii_letters + string.digits + "!@#"
    return ''.join(random.choice(chars) for _ in range(length))

def check_strength(password):
    if len(password) >= 10:
        return "Strong"
    elif len(password) >= 6:
        return "Medium"
    else:
        return "Weak"

length = int(input("Enter password length: "))
pwd = generate_password(length)

print("Generated Password:", pwd)
print("Strength:", check_strength(pwd))