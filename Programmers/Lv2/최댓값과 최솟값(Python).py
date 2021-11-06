import sys
sys.setrecursionlimit(10**8)

answer = [0, 0]

def isSame(arr, x, y, n):
    value = arr[x][y] 
    for i in range(x, x+n):
        for j in range(y, y+n):
            if value != arr[i][j]:
                return False
    
    return True

def compress(arr, x, y, n):
    global answer
    print(x, y, n)
    if not isSame(arr, x, y, n):
        nn = n//2
        compress(arr, x, y, nn)
        compress(arr, x, y+nn, nn)
        compress(arr, x+nn, y, nn)
        compress(arr, x+nn, y+nn, nn)
    else:
        answer[arr[x][y]] += 1

def solution(arr):
    n = len(arr)
    compress(arr, 0, 0, n)
    return answer

print(solution([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]))