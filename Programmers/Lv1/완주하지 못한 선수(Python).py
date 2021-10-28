def solution(participant, completion):
    dic = {}
    # dict에 추가
    for comp in completion:
        if comp in dic:
            dic[comp] += 1
        else:
            dic[comp] = 1

    # 참가자 확인
    for part in participant:
        if part in dic:
            if dic[part] > 0:
                dic[part] -= 1
            else:
                return part
        else:
            return part
            

# Counter을 이용한 풀이

# from collections import Counter

# def solution(participant, completion):
#     answer = Counter(participant) - Counter(completion)
#     return list(answer)[0]