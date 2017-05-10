import hashlib

first10 = ''
specials = '!@#$%^&*()'
rand_int = 0

def hash_func(var):							#Hashing function
    hasher = 0
    hasher = hashlib.sha256()
    hasher.update(var)
    hashvalue = hasher.hexdigest()
    return hashvalue

def rot(c,n):								#Rotation function
    new_ord = ord(c) + (n % 26)
    if c.islower():
        if new_ord > ord('z'):
            new_ord -= 26
        elif new_ord < ord('a'):
            new_ord += 26
        return chr(new_ord)
    return c

def random_int(p):							#Random integer function
	for n in p:
		if n.isdigit():
			print n
			return int(n)

domain = raw_input("Domain: ")
master_pass = raw_input("Master Password: ")

hashed_domain = hash_func(domain)			#Hash domain
hashed_master_pass = hash_func(master_pass)	#Hash master password

password = hashed_domain + hashed_master_pass

for i in range(256):
	password = hash_func(password)			#Perform 256 rounds of sha256

rand_int = random_int(password)				#Set value of random integer

for letter in password[rand_int:rand_int+10]:
	first10 = first10 + rot(letter, rand_int + 10)

final_password = first10.upper() + password[rand_int + 10:rand_int + 20]

final_password = final_password.replace(final_password[rand_int + 10], specials[rand_int], 2)

print final_password

