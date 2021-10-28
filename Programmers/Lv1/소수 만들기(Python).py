def solution(participant, completion):
    dict = {}
    for comp in completion:
        dict[comp] += 1

    for part in participant:
        try:
            if dict[part] > 0:
                dict[part] -= 1
            else:
                return part
        except:
            return part