"""
이 문제는 단순 구현으로 풀었다.
이 문제에서 유의할 점은 회전하는데 있어 어떤 방식으로 저장할지이다.
회전에서 이전 값을 유지하면서 저장하기 위해서는 맨 처음 값을 저장하고 아래로 차곡차곡 저장하는 방식을 이용하는 것이 좋다.
그러한 방식으로 구현하면 큰 문제없이 해결가능하다.
"""
import sys          

def solution(rows, columns, queries):
    answer = []
    arr = [[i*columns+j for j in range(1, columns+1)] for i in range(0, rows)]

    for sx, sy, ex, ey in queries:
        sx, sy, ex, ey = sx-1, sy-1, ex-1, ey-1
        temp = arr[sx][sy]
        arrMin = temp
        
        
        for i in range(sx+1, ex+1):
            arr[i-1][sy] = arr[i][sy]
            arrMin = min(arrMin, arr[i][sy])
            
        for i in range(sy+1, ey+1):
            arr[ex][i-1] = arr[ex][i]
            arrMin = min(arrMin, arr[ex][i])
            
        for i in range(ex-1, sx-1, -1):
            arr[i+1][ey] = arr[i][ey]
            arrMin = min(arrMin, arr[i][ey])
            
        for i in range(ey-1, sy-1, -1):
            arr[sx][i+1] = arr[sx][i]
            arrMin = min(arrMin, arr[sx][i])
            
        arr[sx][sy+1] = temp
        answer.append(arrMin)
    
    return answer