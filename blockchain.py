import json
from block import Block

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.difficulty = 1
    
    def create_genesis_block(self):
        genesis_block = Block(0,"23/02/2024","Genesis Block","0")
        genesis_block.compute_hash()
        genesis_block.isMined = True
        return  genesis_block
    
    def get_latest_block(self):
        return self.chain[-1]
    
    def add_block(self, new_block):
        new_block.previous_hash = self.get_latest_block().compute_hash()
        new_block.proof_of_work(self.difficulty)
        self.chain.append(new_block)
        return True