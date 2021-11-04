def makeIndex():
    index = {}
    for i in range(26):
        index[chr(ord('A')+i)] = i+1
        
    return index

def solution(msg):
    answer = []
    idx = 26
    index = makeIndex()
    
    i = 0
    while i < len(msg):  
        s = msg[i]

        while i < len(msg):
            if s+msg[i+1] in index:
                print(answer, s, i)
                if i == len(msg)-1:
                    answer.append(index[s])
                    break
                else:
                    i += 1
                    s += msg[i]
            else:
                idx += 1
                answer.append(index[s])
                index[s+msg[i+1]] = idx
                i += 1
                break
        
    return answer
print(solution("KAKAO"))