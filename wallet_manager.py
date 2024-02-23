from wallet import Wallet

class Wallet_manager:
    def __init__(self):
        self.wallets = []
    
    def create_wallet(self):
        wallet = Wallet()
        print("your private key is: " + wallet.private_key)
        self.wallets.append(wallet)
    
    def deposit(self, public_key, amount):
        for wallet in self.wallets:
            if(wallet.public_key == public_key):
                wallet.deposit(amount)
    
    def withdraw(self, private_key, amount):
        for wallet in self.wallets:
            if(wallet.private_key == private_key):
                wallet.withdraw(amount, private_key)
    
    def get_balance(self, public_key):
        for wallet in self.wallets:
            if(wallet.public_key == public_key):
                return wallet.get_balance()
    
    def get_wallets(self):
        return self.wallets   
    
    def print_private_keys(self):
        for wallet in self.wallets:
            print(wallet.private_key)