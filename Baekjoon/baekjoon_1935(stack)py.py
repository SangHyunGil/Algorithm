import sys
from collections import deque
input = sys.stdin.readline

def solve():
    for _ in range(int(input())):
        cnt = 1
        n, m = map(int, input().split())
        paper = list(map(int, input().split()))
        queue = deque(zip(paper, range(n)))
        priority = sorted(paper)
        
        while True:
            temp = queue.popleft()
            if temp[0] == priority[-1]:       
                priority.pop()
                if temp[1] == m:
                    print(cnt)
                    break
                cnt += 1
            else:
                queue.append(temp)

solve()