class Node(object):
     def __init__(self,key, value):
         self.value = value
         self.key = key
         self.prev = None
         self.next = None

class LRU_Cache(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.current_count = 0
        self.__cache = {}
        self.most_recently_used = None
        self.least_recently_used  = None
    def removeFromEnd(self):
        if self.least_recently_used == None and self.most_recently_used == None:
            return
        
        if self.current_count == 1:
            keyForEnd = self.least_recently_used.key
            self.least_recently_used = None
            self.most_recently_used = None
        else:
            self.least_recently_used = self.least_recently_used.prev
            keyForEnd = self.least_recently_used.next.key
            self.least_recently_used.next.prev = None
            self.least_recently_used.next = None
        del self.__cache[keyForEnd]
        self.current_count -= 1

    def checkForOverCapicity(self):
        while self.current_count >= self.capacity:
            self.removeFromEnd()
    def addNodeToFront(self, curNode):
        if  self.most_recently_used == None and self.least_recently_used == None:
            self.most_recently_used = curNode
            self.least_recently_used = curNode
            return
        curNode.next = self.most_recently_used
        self.most_recently_used.prev = curNode
        self.most_recently_used = curNode     

    def set(self, key, value):
        if key in self.__cache:
            return
        self.checkForOverCapicity()
        self.current_count += 1
        curNode = Node(key,value)
        self.__cache[key] = curNode
        self.addNodeToFront(curNode)
    def show(self):
        cur = self.most_recently_used
        while cur:
            print(cur.value)
            cur = cur.next
    def get(self,key):
        if key not in self.__cache:
            return -1
        curNode = self.__cache[key]
        if self.most_recently_used != curNode:
            if curNode == self.least_recently_used:
                self.least_recently_used = curNode.prev
            if curNode.next == None:
                curNode.prev.next = None
            else:
                curNode.prev.next = curNode.next
                curNode.next.prev = curNode.prev
            curNode.next = None
            curNode.prev = None
            curNode.next = self.most_recently_used
            self.most_recently_used.prev = curNode
            self.most_recently_used = curNode
        return curNode.value

myLRU = LRU_Cache(3)
myLRU.set(1,1)
myLRU.set(2,2)
myLRU.set(3,3)
myLRU.set(4,4)
myLRU.set(5,5)
print(myLRU.get(1))
print(myLRU.get(5))
myLRU.show() # should print 5, 4 in that order


myLRU2 = LRU_Cache(1)
myLRU2.set(1,1)
myLRU2.set(2,2)
myLRU2.set(3,3)
myLRU2.set(4,4)
myLRU2.set(5,5)
print(myLRU2.get(1))
print(myLRU2.get(5))
myLRU2.show() # should print 5


myLRU2 = LRU_Cache(5)
myLRU2.set(1,1)
myLRU2.set(2,2)
myLRU2.set(3,3)
myLRU2.set(4,4)
myLRU2.set(5,5)
print(myLRU2.get(1))
print(myLRU2.get(5))
myLRU2.show() # should print 5,1,4,3,2
myLRU2.set(None,'33333') # can work. We can put a restriction on this.
print(myLRU2.get(None)) #prints 33333
myLRU2.set('','blank') # can work. We can put a restriction on this.
print(myLRU2.get('')) #prints blank