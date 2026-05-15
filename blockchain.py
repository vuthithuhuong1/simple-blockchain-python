import hashlib
import datetime

class Block:
    def __init__(self, data, previous_hash):
        self.data = data
        self.previous_hash = previous_hash 
        self.timestamp = str(datetime.datetime.now())
        self.hash = self.create_hash()

    def create_hash(self):
        text = self.data + self.timestamp + self.previous_hash
        return hashlib.sha256(text.encode()).hexdigest()
    
block1 = Block("A sends B 10 coins", "0")
block2 = Block("C sends D 5 coins", block1.hash)

print("----- BLOCK 1 -----")
print("Data:", block1.data)
print("Time:", block1.timestamp)
print("Previous Hash:", block1.previous_hash)
print("Hash:", block1.hash)

print("\n----- BLOCK 2 -----")
print("Data:", block2.data)
print("Time:", block2.timestamp)
print("Previous Hash:", block2.previous_hash)
print("Hash:", block2.hash)