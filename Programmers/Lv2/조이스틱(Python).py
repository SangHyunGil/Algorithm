"""
그리디하게 푸는 문제였다.
상하로도 그리디하게 결정해야 하는 문제가 있지만(위 방향키가 더 가까운지, 아래 방향키가 더 가까운지)
좌우로도 그리디하게 결정해야 하는 문제가 있다.(오른쪽으로 가는 숫자가 더 가까운지, 왼쪽으로 가는 숫자가 더 가까운지)
이러한 부분에 대해 각각 나누어 계산을 진행해보았다.
처음에 최솟값들을 미리 전부 구해놓고
좌우로 탐색을 매번 진행하면서 이를 탐색했다.
name의 길이가 20이라 충분히 브루트포스하게 매번 탐색마다 좌우 최소길이를 찾아가며
진행해도 무방했다.
"""

def solution(name):
    alpha = {chr(ord('A')+i) : i+1 for i in range(26)}
    value = [min(alpha[name[i]]-1, 27-alpha[name[i]]) for i in range(len(name))]

    answer, idx = 0, 0
    cnt = len(name) - value.count(0)
    while cnt:
        left = [idx, 0]
        while not value[left[0]]:
            left[1] += 1
            left[0] = (left[0]-1)%len(name)
            
        right = [idx, 0]
        while not value[right[0]]:
            right[1] += 1
            right[0] = (right[0]+1)%len(name)
            
        m = min(right, left, key = lambda x : x[1])
        answer += value[m[0]] + m[1]
        value[m[0]] = 0
        cnt -= 1
        idx = m[0]
        
    return answer