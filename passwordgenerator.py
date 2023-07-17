import random
import string

n = int(input("Enter the size of password:"))
letters = string.ascii_letters
digit = string.digits
punc = string.punctuation

password = ''.join(random.SystemRandom().choice(punc + letters + digit) for _ in range(n))

print("Your password is ready: ", password)