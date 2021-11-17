import sys
from itertools import permutations
input = sys.stdin.readline

def solve():
    num = [0] * 9

    for room_num in (input().strip()):
        if int(room_num) == 9:
            num[6] += 1
            continue
        num[int(room_num)] += 1
    
    if num[6] % 2 == 0:
        num[6] = num[6]//2
    else:
        num[6] = num[6]//2+1
    
    print(max(num))

solve()