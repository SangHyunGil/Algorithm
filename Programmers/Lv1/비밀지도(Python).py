def makeMap(s):
    s = list(s)
    for i in range(len(s)):
        s[i] = '#' if s[i] == '1' else ' '
        
    return "".join(s)

def solution(n, arr1, arr2):
    answer = []
    for a1, a2 in zip(arr1, arr2):
        # or 연산을 활용한 합치기 후 지도로 변형
        temp = makeMap(format(a1 | a2, 'b').zfill(n))
        answer.append(temp)
    
    return answer