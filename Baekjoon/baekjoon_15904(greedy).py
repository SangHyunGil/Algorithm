"""
단순히 브루트포스로 풀면된다.
앞에서부터 일치하는 문자가 있는지 확인하면서 지우고
UCPC가 모두 지워졌다면 옳고 아니라면 틀린것이다.
"""
import sys
sys = sys.stdin.readline

ucpc = ["C", "P", "C", "U"]
s = input().strip()

for c in s:
    if ucpc and ucpc[-1] == c:
        ucpc.pop()

print("I hate UCPC" if ucpc else "I love UCPC")