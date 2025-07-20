import os 
import json 
import random
import time
from getpass import getpass
from user import User



class BankSystem:
    def __init__(self, user_file='users.json'):
        self.user_file = user_file
        self.users = self.load_users()

    # Initialize the bank system with a user file
    # If the user file does not exist, it will be created
    def load_users(self):
        if not os.path.exists(self.user_file):
            with open(self.user_file, 'w') as f:
                json.dump({}, f)
        with open(self.user_file, 'r') as f:
            return json.load(f)

    # Save users to the JSON file
    def save_users(self):
        with open(self.user_file, 'w') as f:
            json.dump(self.users, f, indent=4)

    # Generate a unique account number
    def generate_account_number(self):
        existing_acc_nums = {details['account_number'] for details in self.users.values()}
        while True:
            acc_num = str(random.randint(1000000000, 9999999999))
            if acc_num not in existing_acc_nums:
                return acc_num
    #  SIGN UP FUNCTION
    def sign_up(self):
        print('\n' + '*' * 35)
        print('== 🏦 Assassin Bank Sign Up ==')
        print('*' * 35)

        first_name = input('Enter your first name: ').strip().capitalize()
        last_name = input('Enter your last name: ').strip().capitalize()

        # username collection and validation
        while True:
            username = input('Choose a username: ').strip()
            if username in self.users:
                print('Username already exists. Please choose a different username.')
            else:
                break

        # password visibility choice
        while True:
            visibility_choice = input('Do you want your password hidden while typing? (y/n): ').strip().lower()
            if visibility_choice in ('y', 'n'):
                break
            else:
                print('Invalid choice. Please enter "y" or "n".')

        # password collection and validation
        while True:
            password = getpass('Enter your password: ') if visibility_choice == 'y' else input('Enter your password: ')
            if len(password) < 8:
                print('Password must be at least 8 characters long. Please try again.')
                continue
            if not any(char.isdigit() for char in password):
                print('Password must contain at least one digit. Please try again.')
                continue
            if not any(char.isalpha() for char in password):
                print('Password must contain at least one letter. Please try again.')
                continue
            if not any(char in '!@#$%^&*()_+-=[]{}|;:,.<>?/' for char in password):
                print('Password must contain at least one special character. Please try again.')
                continue
            
            confirm_password = getpass('Confirm your password: ') if visibility_choice == 'y' else input('Confirm your password: ')
            if password != confirm_password:
                print('Passwords do not match. Please try again.')
            else:
                break

        # pin collection and validation
        while True:
            pin = getpass('Enter a 4-digit PIN: ') if visibility_choice == 'y' else input('Enter a 4-digit PIN: ')
            if len(pin) != 4 or not pin.isdigit():
                print('PIN must be exactly 4 digits. Please try again.')
                continue
            confirm_pin = getpass('Confirm your PIN: ') if visibility_choice == 'y' else input('Confirm your PIN: ')
            if pin != confirm_pin:
                print('PINs do not match. Please try again.')
            else:
                break

        # account creation 
        print('\nCreating your account...')
        time.sleep(2)  # Simulate account creation delay
        print('Please wait...')
        time.sleep(2)  # Simulate processing delay
        print('Almost done...')
        time.sleep(3)  # Simulate final processing delay
        
        account_number = self.generate_account_number()
        user = User(
            first_name=first_name,
            last_name=last_name,
            username=username,
            password=password,
            pin=pin,
            account_number=account_number
        )
        self.users[username] = user.to_dict()
        self.save_users()

        print('\n' + '*' * 35)
        print('== Account Created Successfully! ==') 
        print('*' * 35)
        print(f'Welcome to Assassin Bank, {first_name} {last_name}!')
        print(f'Your username is: {username}')
        print(f'Your account number is: {account_number}')
        # print('Please remember your account number and username for future logins.')
        print('You can now log in to your account.\n')
        input('Press Enter to continue...')
        

    # def sign_up(self, username, password):
    #     if username in self.users:
    #         return False
    #     self.users[username] = password
    #     return True

    # def log_in(self, username, password):
    #     return self.users.get(username) == password

    # def load_user(self, username):
    #     return self.users.get(username)