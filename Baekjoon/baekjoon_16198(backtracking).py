from collections import deque

def bfs(begin, target, words):
    queue = deque([list(begin)])
    visited = dict()
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    while queue:
        word = queue.popleft()

        for i in range(len(word)):
            temp = word
            for alpha in alphabet:
                temp[i] = alpha
                print("".join(temp))


def solution(begin, target, words):
    answer = 0

    bfs(begin, target, words)

    return answer