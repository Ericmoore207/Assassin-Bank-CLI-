import hashlib 

class User:
    def __init__(self, first_name, last_name, username, account_number, password, pin, balance=0, transactions=[]):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.account_number = account_number
        self.password = password
        self.pin = pin
        self.balance = balance
        self.transactions = [] # transactions if transactions is not None else []

    def hash_data(self, data):
        """Hash the user's password using SHA-256."""
        return hashlib.sha256(data.encode()).hexdigest() 
    
    def to_dict(self):
        """Convert the User object to a dictionary."""
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "username": self.username,
            "account_number": self.account_number,
            "password": self.password,  # Note: This should not be stored in plaintext in production
            "pin": self.pin,  # Note: This should also be hashed in production
            "balance": self.balance,
            "transactions": self.transactions
        }