import hashlib

first10 = ''
specials = '!@#$%^&*()'
count = 0

def hash_func(var):
    hasher = 0
    hasher = hashlib.sha256()
    hasher.update(var)
    hashvalue = hasher.hexdigest()
    return hashvalue

def rot(c,n):
    """ rotate c forward by n characters,
        wrapping as needed; only letters change
    """
    new_ord = ord(c) + (n % 26)
    if c.islower():
        if new_ord > ord('z'):
            new_ord -= 26
        elif new_ord < ord('a'):
            new_ord += 26
        return chr(new_ord)
    return c

domain = raw_input("Domain: ")
master_pass = raw_input("Master Password: ")

combined_pass = domain + master_pass

password = hash_func(combined_pass)

for letter in password[0:9]:
	first10 = first10 + rot(letter, 15)

for i in range(9):
	if first10[i].isdigit():
		final_password = first10.replace(first10[i], specials[int(first10[i])])
		break;

final_password = final_password.upper() + password[10:18]

print final_password

