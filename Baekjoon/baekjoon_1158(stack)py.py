import sys, time
from collections import deque
input = sys.stdin.readline

class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList():
    def __init__(self):
        self.head = Node(1)
        self.head.next = self.head
        self.size = 1

answer = "<"
link = CircularLinkedList()
N, K = map(int, input().split())

target = link.head
for i in range(2, N+1):
    newNode = Node(i)
    target.next = newNode
    newNode.next = link.head
    target = target.next
    link.size += 1

target = link.head
while link.size:
    cnt = K-2
    while cnt:
        target = target.next
        cnt -= 1
        
    store = target.next
    answer += str(store.data) + (", " if link.size != 1 else "")
  
    store = store.next
    target.next = store
    target = store
    link.size -= 1


answer += ">"
print(answer)