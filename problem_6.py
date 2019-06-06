
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next
        return size

def union(llist_1, llist_2):
    mySet = set()
    cur1 = llist_1.head
    seen = {}
    listToReturn =  LinkedList()
    while cur1 != None:
        mySet.add(cur1.value)
        cur1 = cur1.next
    cur2 = llist_2.head
    while cur2 != None:
        if cur2.value in mySet and cur2.value not in seen:
            seen[cur2.value] = True
            listToReturn.append(cur2.value)
        cur2 = cur2.next
    return listToReturn

def intersection(llist_1, llist_2):
    mySet = set()
    cur1 = llist_1.head
    listToReturn =  LinkedList()
    while cur1 != None:
        mySet.add(cur1.value)
        cur1 = cur1.next
    cur2 = llist_2.head
    while cur2 != None:
        mySet.add(cur2.value)
        cur2 = cur2.next
    for value in mySet:
        listToReturn.append(value)
    return listToReturn

# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))
print (intersection(linked_list_1,linked_list_2))

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print(union(linked_list_3,linked_list_4))
print(intersection(linked_list_3,linked_list_4))


linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_1 = [5,2,6,55,6,65,6,6,5,25]
element_2 = []

for i in element_1:
    linked_list_5.append(i)

for i in element_2:
    linked_list_6.append(i)
print('_______')
print(union(linked_list_5,linked_list_6)) # should print nothing, because there are no matches!
print('_______')
print(intersection(linked_list_5,linked_list_6))

linked_list_7 = LinkedList()
linked_list_8 = LinkedList()

element_1 = []
element_2 = []

for i in element_1:
    linked_list_7.append(i)

for i in element_2:
    linked_list_8.append(i)
print('_______')
print(union(linked_list_7,linked_list_8)) # should print nothing
print('_______')
print(intersection(linked_list_7,linked_list_8)) # should print nothing