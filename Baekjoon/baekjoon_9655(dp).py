import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
print("CY" if n % 2 == 0 else "SK")