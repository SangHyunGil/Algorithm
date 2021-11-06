def makeIndex():
    index = {}
    for i in range(26):
        index[chr(ord('A')+i)] = i+1
        
    return index

def solution(msg):
    answer = []
    idx = 26
    index = makeIndex()
    
    
    while msg:  
        i = 1
        while i <= len(msg) and msg[:i] in index:
            i += 1
        
        i -= 1
        print(answer, msg, i)
        if msg[:i] in index:
            idx += 1
            answer.append(index[msg[:i]])
            index[msg[:i+1]] = idx
            
        msg = msg[i:]
        
    return answer

print(solution("KAKAO"))
print(solution("ABABABABABABABAB"))