import sys
from itertools import permutations
input = sys.stdin.readline

class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)

class LinkedList():
    def __init__(self):
        self.head = Node("dummy")
        self.size = 0

    def sizes(self):
        return self.size

    def isEmpty(self):
        return False if self.size else True
    
    def find(self, idx):
        if self.size == 0 or idx >= self.size :
            return IndexError
        else:
            store = self.head
            for i in range(idx):
                store = store.next
            return store

    def appendleft(self, data):
        newNode = Node(data)
        store = self.head.next
        self.head.next = newNode
        newNode.next = store
        self.size += 1

    def append(self, data):
        newNode = Node(data)
        store = self.head
        while store.next != None:
            store = store.next
        store.next = newNode
        self.size += 1

    def insert(self, idx, data):
        if idx >= self.size:
            return IndexError
        newNode = Node(data)
        store = self.head
        for i in range(idx):
            store = store.next
        temp = store.next
        store.next = newNode
        newNode.next = temp

    def delete(self, idx):
        if self.size == 0 or idx >= self.size:
            return IndexError
        else:
            store = self.head
            for i in range(idx):
                store = store.next
            temp = store.next.next
            store.next = temp
            self.size -= 1

    def __str__(self):
        s = ""
        store = self.head.next
        while store.next:
            s += str(store.data) + " -> "
            store = store.next
        s += str(store.data)
        return s
    
link = LinkedList()
for i in range(4):
    link.append(i)

print(link) # LinkedList 출력
print(link.sizes()) # LinkedList 사이즈
print(link.isEmpty()) # LInkedList Empty 확인
print(link.delete(1))
print(link)
print(link.sizes())