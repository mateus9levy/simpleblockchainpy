import hashlib
import json

class Block:
    def __init__(self,index,timestamp,transactions,previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.nonce = 0
        self.isMined = False

    def compute_hash(self):
        if(self.isMined):
            return self.hash
        block_string = json.dumps(self.__dict__,sort_keys=True)
        hash = hashlib.sha256(block_string.encode()).hexdigest()
        self.hash = hash
        return hash
    
    def proof_of_work(self, difficulty):
        while self.compute_hash()[:difficulty] != '0'*difficulty:
            self.nonce += 1
        hash = self.compute_hash()
        self.hash = hash
        self.isMined = True
        return hash
    
    def __str__(self):
        return f"""Index: {self.index}
Timestamp: {self.timestamp}
Transactions: {self.transactions}
Previous Hash: {self.previous_hash}
Hash: {self.hash}
Nonce: {self.nonce}"""
    