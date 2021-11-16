def getMax(land, i, j):
    num = {0, 1, 2, 3}
    return max([land[i-1][k]+land[i][j] for k in num if j != k])

def solution(land):
    for i in range(1, len(land)):
        for j in range(4):
            land[i][j] = getMax(land, i, j)
    
    return max(land[-1])