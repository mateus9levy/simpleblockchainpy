import uuid
import hashlib
class Wallet:
    def __init__(self):
        self.balance = 0
        self.private_key = self.generate_private_key()
        self.public_key = self.generate_public_key()

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount, private_key):
        if(private_key != self.private_key):
            return "Invalid private key"
        else:
            self.balance -= amount
    
    def generate_public_key(self):
        hashed_private_key = hashlib.sha256(self.private_key.encode()).hexdigest()
        return hashed_private_key

    def get_balance(self):
        return self.balance
    
    def generate_private_key(self):
        private_key = "0x" + str(uuid.uuid4()).replace("-","")
        return private_key
    
    def __str__(self):
        return f"Balance: {self.balance}\nPublic Key: {self.public_key}"