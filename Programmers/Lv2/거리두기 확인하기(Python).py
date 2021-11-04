"""
bfs로 각 p에 대해서 전체 순회해준다.
단, 주의해야할 점은 시작 점 p를 제외하고 도착점 p는 visited 처리해주면 안된다.
왜냐하면 해당 p로 갈 수 있는 경우의 수는 여러가지이다.
그러기에, 가는 경로에 한해서만 visited 처리해주어 다른 경로에 대해서도 체크하도록 해준다.
"""

from collections import deque

def isValid(i, j):
    if 0 <= i < 5 and 0 <= j < 5:
        return True
    else:
        return False

def bfs(place, visited, i, j):
    queue = deque([[i, j, 0, False]])
    visited[i][j] = 1
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    while queue:
        x, y, cnt, partition = queue.popleft()

        for k in range(4):
            nx, ny = x+dx[k], y+dy[k]

            if cnt < 2 and isValid(nx, ny) and not visited[nx][ny]:
                if place[nx][ny] == 'X':
                    visited[nx][ny] = 1
                    queue.append([nx, ny, cnt+1, True])

                elif place[nx][ny] == 'O':
                    visited[nx][ny] = 1
                    queue.append([nx, ny, cnt+1, False])
                
                else:
                    if abs(i-nx) + abs(j-ny) <= 2 and not partition:
                        return 1
                    else:
                        queue.append([nx, ny, cnt+1, partition])

    return 0

def isSafe(place, visited):
    for i in range(5):
        for j in range(5):
            if place[i][j] == 'P' and not visited[i][j]:
                if bfs(place, visited, i, j):
                    return 0

    return 1

def solution(places):
    answer = []

    for place in places:
        visited = [[0] * 5 for _ in range(5)]
        answer.append(1 if isSafe(place, visited) else 0)
        
    return answer


print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))