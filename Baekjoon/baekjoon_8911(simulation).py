"""
단순한 구현문제이다.
방향 전환과 전진을 하면서 각 좌표의 최대 최소를 구해 가로 길이와
세로 길이를 구해 넓이를 계산한다.
문제를 제대로 읽지 않아 계속적인 실수가 발생했다.
문제를 좀 더 꼼꼼히 읽는 습관을 들이자.
"""
import sys
input = sys.stdin.readline
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for i in range(int(input())):
    storeX, storeY = [0], [0]
    d, cx, cy = 0, 0, 0
    for cmd in list(input().rstrip()):
        if cmd == 'F':
            cx, cy = cx+dx[d], cy+dy[d] 
            storeX.append(cx)
            storeY.append(cy)

        elif cmd == 'B':
            cx, cy = cx-dx[d], cy-dy[d]
            storeX.append(cx)
            storeY.append(cy)

        elif cmd == 'L':
            d = (d-1)%4

        else:
            d = (d+1)%4
    
    print((max(storeX)-min(storeX))*(max(storeY)-min(storeY)))