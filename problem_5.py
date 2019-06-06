

import hashlib
import time


class List:
    def __init__(self):

        self.previous_hash = None
        self.list = {}
    
    def add(self, data):
        newBlock = Block(time.time(), data, self.previous_hash)
        self.list[newBlock.hash] = newBlock
        self.previous_hash  = newBlock.hash
        return newBlock.hash

class Block:

    def __init__(self, timestamp, data, previous_hash):
      self.timestamp = timestamp
      self.data = data
      self.previous_hash = previous_hash
      self.hash = self.calc_hash()

    def calc_hash(self):
      sha = hashlib.sha256()
      sha.update(hex(id(self)).encode())
      return sha.hexdigest()

myList =  List()
hash1 = myList.add('1') 
print(len(myList.list) == 1) # Should be one.
print(myList.list[hash1].previous_hash == None)

hash2 = myList.add('here you go 2')
print(len(myList.list) == 2)
print(myList.list[hash2].previous_hash == hash1)

hash3 = myList.add('heres 3')
print(len(myList.list) == 3)
print(myList.list[hash3].previous_hash == hash2)

hash4 = myList.add('heres 4')
print(len(myList.list) == 4)
print(myList.list[hash4].previous_hash == hash3)



print(myList.list)