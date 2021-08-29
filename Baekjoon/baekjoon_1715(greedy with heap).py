import sys, time
from collections import deque
input = sys.stdin.readline

def isPrevious(start_month, start_day, end_month, end_day):
    if start_month < end_month:
        return True
    elif start_month == end_month and start_day <= end_day:
        return True
    
    return False

answer = 0
n = int(input())
flowers = deque(sorted([list(map(int, input().split())) for _ in range(n)]))

if flowers[0][0] > 3 or (flowers[0][0] == 3 and flowers[0][1] > 1) or (flowers[0] == [3, 1, 3, 1]):
    print(0)
    sys.exit(0)

end_month, end_day = 3, 1
while flowers:
    length = len(flowers)
    if end_month > 11:
        break
    
    store_month, store_day = 0, 0
    while flowers and isPrevious(flowers[0][0], flowers[0][1], end_month, end_day):
        flower = flowers.popleft()
        
        if (store_month, store_day) < (flower[2], flower[3]):
            store_month, store_day = flower[2], flower[3]

    if length == len(flowers):
        break

    end_month, end_day = store_month, store_day
    answer += 1

print(answer if end_month > 11 else 0)