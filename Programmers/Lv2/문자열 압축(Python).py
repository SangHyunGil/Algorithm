def solution(record):
    answer = []
    
    user = {}
    for rec in record:
        rec = rec.split()
        if rec[0] == "Enter":
            user[rec[1]] = rec[2]
            answer.append(user[rec[1]]+"님이 들어왔습니다.")
        elif rec[0] == "Change":
            user[rec[1]] = rec[2]
        else:
            del user[rec[1]]
            answer.append(user[rec[1]]+"님이 나갔습니다.")
        

    return answer

solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"])