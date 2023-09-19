import datetime
import hashlib


class Block:
    def __init__(self,previous_block_hash,transaction,timestamp):
        self.previous_block_hash=previous_block_hash
        self.transaction=transaction
        self.timestamp=timestamp
        self.hash=self.get_hash()

    #创建创世块
    @staticmethod
    def create_genesis_block():
        return Block('0','0',datetime.datetime.now())

    def get_hash(self):
        header_bin = str(self.previous_block_hash)+str(self.transaction)+str(self.timestamp)
        out_hash = hashlib.sha256(header_bin.encode()).hexdigest()
        return out_hash
    
    #工作量证明
    @staticmethod
    def proof_of_work(last_proof):
        proof = 0
        while not Block.is_valid_proof(last_proof, proof):
            proof += 1
        return proof

    @staticmethod
    def is_valid_proof(last_proof, proof):
        guess = f"{last_proof}{proof}".encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"  
