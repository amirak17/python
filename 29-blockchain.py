import hashlib
import time
import json

class Block:
    def __init__(self, index, timestamp, data, previous_hash, nonce=0):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = nonce
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = json.dumps({
            "index": self.index,
            "timestamp": self.timestamp,
            "data": self.data,
            "previous_hash": self.previous_hash,
            "nonce": self.nonce
        }, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

class Blockchain:
    def __init__(self, difficulty=4):
        self.chain = []
        self.difficulty = difficulty  # Number of leading zeros required in hash
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis_block = Block(0, time.time(), "Genesis Block", "0")
        self.mine_block(genesis_block)
        self.chain.append(genesis_block)

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, data):
        new_block = Block(
            index=len(self.chain),
            timestamp=time.time(),
            data=data,
            previous_hash=self.get_latest_block().hash
        )
        self.mine_block(new_block)
        self.chain.append(new_block)

    def mine_block(self, block):
        target = "0" * self.difficulty
        while block.hash[:self.difficulty] != target:
            block.nonce += 1
            block.hash = block.calculate_hash()
        print(f"Block mined! Nonce: {block.nonce}, Hash: {block.hash}")

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]

            # Verify current block's hash
            if current_block.hash != current_block.calculate_hash():
                print(f"Invalid hash in block {i}")
                return False

            # Verify previous block's hash
            if current_block.previous_hash != previous_block.hash:
                print(f"Chain broken at block {i}")
                return False

            # Verify proof of work
            if current_block.hash[:self.difficulty] != "0" * self.difficulty:
                print(f"Invalid proof of work in block {i}")
                return False

        return True

# Example usage
if __name__ == "__main__":
    my_blockchain = Blockchain(difficulty=4)

    print("Adding Block 1...")
    my_blockchain.add_block({"transaction": "Alice pays Bob 10 BTC"})
    
    print("\nAdding Block 2...")
    my_blockchain.add_block({"transaction": "Bob pays Charlie 5 BTC"})

    print("\nBlockchain valid?", my_blockchain.is_chain_valid())

    # Print the blockchain
    for block in my_blockchain.chain:
        print(f"\nBlock #{block.index}")
        print(f"Timestamp: {block.timestamp}")
        print(f"Data: {block.data}")
        print(f"Previous Hash: {block.previous_hash}")
        print(f"Hash: {block.hash}")
        print(f"Nonce: {block.nonce}")

    # Test tampering with the blockchain
    print("\nTampering with Block 1...")
    my_blockchain.chain[1].data = {"transaction": "Alice pays Bob 100 BTC"}
    print("Blockchain valid after tampering?", my_blockchain.is_chain_valid())