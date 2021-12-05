import sys
input = sys.stdin.readline

def preOrder(tree, node):
    if node != '.':
        print(node, end="")
        preOrder(tree, tree[node][0])
        preOrder(tree, tree[node][1])

def inOrder(tree, node):
    if node != '.':
        inOrder(tree, tree[node][0])
        print(node, end="")
        inOrder(tree, tree[node][1])

def postOrder(tree, node):
    if node != '.':
        postOrder(tree, tree[node][0])
        postOrder(tree, tree[node][1])
        print(node, end="")

def show(tree):
    preOrder(tree, 'A')
    print()
    inOrder(tree, 'A')
    print()
    postOrder(tree, 'A')

tree = {}
n = int(input())
for i in range(n):
    root, left, right = input().split()
    tree[root] = [left, right]

show(tree)