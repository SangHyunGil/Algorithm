import sys
from collections import deque
input = sys.stdin.readline

print("CY" if int(input().rstrip()) % 2 else "SK")