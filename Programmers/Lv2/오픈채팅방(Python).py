"""
이 문제는 단순히 모든 레코드에 대해 값을 사전에 저장하면서 변경된다면 변경해준다.
그리고 마지막에 단순히 프린트해주면 되는 문제이다.
"""

def solution(record):
    answer = []
    
    user = {};
    for rec in record:
        rec = rec.split()
        if rec[0] == "Enter":
            user[rec[1]] = rec[2]
            answer.append([rec[1], rec[0]])
        elif rec[0] == "Change":
            user[rec[1]] = rec[2]
        else:
            answer.append([rec[1], rec[0]])
    
    result = []
    for ans in answer:
        if ans[1] == "Enter":
            result.append(user[ans[0]]+"님이 들어왔습니다.")
        else:
            result.append(user[ans[0]]+"님이 나갔습니다.")

    return  result