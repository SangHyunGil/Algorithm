import sys
input = sys.stdin.readline

ans = 0
dx = [0, 1]
dy = [1, 0]

def isValid(i, j):
    if 0 <= i < 8 and 0 <= j < 7:
        return True
    else:
        return False

def find(cnt):
    global ans
    if cnt == 28:
        ans += 1
        return

    for x in range(8):
        for y in range(7):
            if not visited[x][y]:
                visited[x][y] = 1
                for k in range(2):
                    nx, ny = x+dx[k], y+dy[k]
                    
                    if isValid(nx, ny) and not visited[nx][ny]: 
                        v1 = graph[x][y]
                        v2 = graph[nx][ny]
                        if alpha[v1][v2] or alpha[v2][v1]:
                            return
                        alpha[v1][v2] = 1
                        visited[nx][ny] = 1             
                        find(cnt+1)
                        alpha[v1][v2] = 0
                        visited[nx][ny] = 0
                visited[x][y] = 0



visited = [[0]*7 for _ in range(8)]
alpha = [[0]*7 for _ in range(7)]
graph = [[*map(int, input().rstrip())] for _ in range(8)]
find(0)
print(ans)