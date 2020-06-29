import hashlib
import json
from check_creds import main
from getpass import getpass

# def is_cred_valid(username, password):
    

username_input = input('Please enter your username:')
password_input = hashlib.sha256(getpass('Please enter your password:').encode()).hexdigest()
while main(username_input,password_input) is False:
    print('get lost or try again: ')
    username_input = input('Please enter your username:')
    password_input = hashlib.sha256(getpass('Please enter your password:').encode()).hexdigest()

