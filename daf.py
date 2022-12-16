#!/usr/bin/env python
import hashlib

common_passwords = []
user_hash_dict = {}
hash = ''
USERNAME = ''
password = ''

class bcolors:
    RED = '\033[91m'

print(bcolors.RED + '''
          _____                    _____                    _____          
         /\    \                  /\    \                  /\    \         
        /::\    \                /::\    \                /::\    \        
       /::::\    \              /::::\    \              /::::\    \       
      /::::::\    \            /::::::\    \            /::::::\    \      
     /:::/\:::\    \          /:::/\:::\    \          /:::/\:::\    \     
    /:::/  \:::\    \        /:::/__\:::\    \        /:::/__\:::\    \    
   /:::/    \:::\    \      /::::\   \:::\    \      /::::\   \:::\    \   
  /:::/    / \:::\    \    /::::::\   \:::\    \    /::::::\   \:::\    \  
 /:::/    /   \:::\ ___\  /:::/\:::\   \:::\    \  /:::/\:::\   \:::\    \ 
/:::/____/     \:::|    |/:::/  \:::\   \:::\____\/:::/  \:::\   \:::\____\ 
\:::\    \     /:::|____|\::/    \:::\  /:::/    /\::/    \:::\   \::/    /
 \:::\    \   /:::/    /  \/____/ \:::\/:::/    /  \/____/ \:::\   \/____/ 
  \:::\    \ /:::/    /            \::::::/    /            \:::\    \     
   \:::\    /:::/    /              \::::/    /              \:::\____\    
    \:::\  /:::/    /               /:::/    /                \::/    /    
     \:::\/:::/    /               /:::/    /                  \/____/     
      \::::::/    /               /:::/    /                                
       \::::/    /               /:::/    /                                
        \::/____/                \::/    /                                 
         ~~                       \/____/       Made By: Void_Security                            ''')

# password_dictionary.txt
with open(input('\nDictionary File Path >> '), 'r') as f:
    common_passwords = f.read().splitlines()

# user_hashes.txt
print('\nDatabase Dump File Format Example | USERNAME:PASSWORDHASH\n')
with open(input('Database Dump File Path >> '), 'r') as f:
    text = f.read().splitlines()
    for user_hash in text:
        USERNAME = user_hash.split(":")[0]
        hash = user_hash.split(":")[1]
        user_hash_dict[USERNAME] = hash

print('\nFormat Options (Currently Limited to Hashlib Module) | md5, sha1, sha224, sha256, sha384, sha512\n')
method = input('Hash Format >> ')

print('\nRunning...\n')

if method == 'md5':
    for password in common_passwords:
        hashed_password = hashlib.md5(password.encode('utf-8')).hexdigest()
        for USERNAME, hash in user_hash_dict.items():
            if hashed_password == hash:
                print(f'CRACKED\n{USERNAME}:{password}\n')
elif method == 'sha1':
    for password in common_passwords:
        hashed_password = hashlib.sha1(password.encode('utf-8')).hexdigest()
        for USERNAME, hash in user_hash_dict.items():
            if hashed_password == hash:
                print(f'CRACKED\n{USERNAME}:{password}\n')
elif method == 'sha224':
    for password in common_passwords:
        hashed_password = hashlib.sha224(password.encode('utf-8')).hexdigest()
        for USERNAME, hash in user_hash_dict.items():
            if hashed_password == hash:
                print(f'CRACKED\n{USERNAME}:{password}\n')
elif method == 'sha256':
    for password in common_passwords:
        hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
        for USERNAME, hash in user_hash_dict.items():
            if hashed_password == hash:
                print(f'CRACKED\n{USERNAME}:{password}\n')
elif method == 'sha384':
    for password in common_passwords:
        hashed_password = hashlib.sha384(password.encode('utf-8')).hexdigest()
        for USERNAME, hash in user_hash_dict.items():
            if hashed_password == hash:
                print(f'CRACKED\n{USERNAME}:{password}\n')
elif method == 'sha512':
    for password in common_passwords:
        hashed_password = hashlib.sha512(password.encode('utf-8')).hexdigest()
        for USERNAME, HASH in user_hash_dict.items():
            if hashed_password == HASH:
                print(f'CRACKED\n{USERNAME}:{password}\n')

