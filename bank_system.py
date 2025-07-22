import os 
import json 
import random
import time
import datetime
from getpass import getpass
from user import User
import hashlib



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

    # Hash Password
    def hash_data(self, data):
        """Hash the user's password using SHA-256."""
        return hashlib.sha256(data.encode()).hexdigest() 
    
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
                print('❌ Username already exists. Please choose a different username.')
            else: 
                break

        # password visibility choice
        while True:
            visibility_choice = input('Do you want your password hidden while typing? (y/n): ').strip().lower()
            if visibility_choice in ('y', 'n'):
                break
            else:
                print('❌ Invalid choice. Please enter "y" or "n".')

        # password collection and validation
        while True:
            
            password = getpass('Enter your password: ') if visibility_choice == 'y' else input('Enter your password: ')
            if len(password) < 8:
                print('❌ Password must be at least 8 characters long. Please try again.')
                continue
            if not any(char.isdigit() for char in password):
                print('❌ Password must contain at least one digit. Please try again.')
                continue
            if not any(char.isalpha() for char in password):
                print('❌ Password must contain at least one letter. Please try again.')
                continue
            if not any(char in '!@#$%^&*()_+-=[]{}|;:,.<>?/' for char in password):
                print('❌ Password must contain at least one special character. Please try again.')
                continue

            
            confirm_password = getpass('Confirm your password: ') if visibility_choice == 'y' else input('Confirm your password: ')
            if password != confirm_password:
                print('❌ Passwords do not match. Please try again.')
            else:
                break

        hash_password = hashlib.sha256(password.encode()).hexdigest()

        # pin collection and validation
        while True:
            pin = getpass('Enter a 4-digit PIN: ') if visibility_choice == 'y' else input('Enter a 4-digit PIN: ')
            if len(pin) != 4 or not pin.isdigit():
                print('❌ PIN must be exactly 4 digits. Please try again.')
                continue
            confirm_pin = getpass('Confirm your PIN: ') if visibility_choice == 'y' else input('Confirm your PIN: ')
            if pin != confirm_pin:
                print('❌ PINs do not match. Please try again.')
            else:
                break

        hash_pin = hashlib.sha256(pin.encode()).hexdigest()

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
            password=hash_password,
            pin=hash_pin,
            account_number=account_number
        )
        self.users[username] = user.to_dict()
        self.save_users()

        print('\n' + '*' * 35)
        print('== ✅ Account Created Successfully! ==') 
        print('*' * 35)
        print(f'Welcome to Assassin Bank, {first_name} {last_name}!')
        print(f'Your username is: {username}')
        print(f'Your account number is: {account_number}')
        print('You can now log in to your account.\n')
        input('\nPress Enter to continue...')

    # LOG IN FUNCTION
    def log_in(self):

        print('\n' + '*' * 35)
        print('== 🏦 Assassin Bank LogIn ==')
        print('*' * 35)
        attempt = 0
        MAX_ATTEMPT = 3

        while attempt < MAX_ATTEMPT :
            username = input('Enter yout Username: ').strip()
            if username not in self.users :
                print('❌ Username not found.\n')
                attempt += 1
                continue

            # password visibility choice
            while True:
                visibility_choice = input('Do you want your password hidden while typing? (y/n): ').strip().lower()
                if visibility_choice in ('y', 'n'):
                    break
                else:
                    print('❌ Invalid choice. Please enter "y" or "n".')


            password = getpass('Enter your password:' ) if visibility_choice == 'y' else input('Enter your password: ')

            hash_password = hashlib.sha256(password.encode()).hexdigest()
            if hash_password != self.users[username]['password']:
                print('❌ Incorrect password ')
                attempt += 1
                continue
            
            print('\nLogining...')
            time.sleep(2)
            print('Please wait...') # Simulate processing delay
            time.sleep(2)  # Simulate final processing delay
            print('✅ Login successful!\n')
            time.sleep(2)

            print('*' * 35)
            print(f'\nWelcome to Assasin Bank, {username}')
            print(f'Account number: {self.users[username]['account_number']}')
            print(f'Balance: ${self.users[username]['balance']}\n')
            print('*' * 35)

            # Create User instance for session
            user_data = self.users[username]
            user = User(
                first_name=user_data['first_name'],
                last_name=user_data['last_name'],
                username=user_data['username'],
                account_number=user_data['account_number'],
                password=password,
                pin=user_data['pin'],
                balance=user_data.get('balance', 0),
                transactions=user_data.get('transactions', [])
            )
            self.user_dashboard(user)
            return
        
        # If too many attempts
        print(' ⚠️Too many failed attempt.')
        time.sleep(2)
        print('Exiting Login...')
        time.sleep(3)
        print('Exiting Login Done!')
        

    def user_dashboard(self, user):
        while True:
            print(' ==🏦 Assassin Bank Dashboard ==')
            print('1. View Balance')
            print('2. Deposit')
            print('3. Withdraw')
            print('4. Transfer')
            print('5. View Transations History ')
            print('6. Forget pin')
            print('7. Logout ')

            choice = input('👉 Choose an option: ')

            if choice == '1':
                self.view_balance(user)

            elif choice == '2':
                self.deposit(user)

            elif choice == '3':
                self.withdraw(user)

            elif choice == '4':
                self.transfer(user)

            elif choice == '5':
                self.view_transations_history(user)
            
            elif choice == '6':
                self.forget_pin(user)

            elif choice == '7':
                print(f'👋 Thanks for banking with us!')
                time.sleep(2)
                print('Logining out...')
                time.sleep(3)
                print('✅ Logout successful!')
                break

            else:
                print('❌ Invalid choice. Try again.')

