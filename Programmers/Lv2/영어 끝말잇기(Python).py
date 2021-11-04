import re

def makeTuple(s):
    tp = s.lstrip('{').rstrip('}').split('},{')
    tp = [t.split(',') for t in tp]
    return tp

def solution(s):
    tp = makeTuple(s)
    print(tp)
    tp.sort(key=lambda x:len(x))

    order = {}
    for t in tp:
        for i in range(len(t)):
            if t[i] not in order:
                order[t[i]] = 1
            else:
                order[t[i]] += 1
    
    return [k for k, _ in sorted(order.items(), key=lambda x:x[1])]
solution("{{20,111},{111}}")