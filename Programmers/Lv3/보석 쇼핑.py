def solution(gems):
    length = len(set(gems))
    answer = []

    jewels = dict()
    left = 0; right = 0
    while left < len(gems):
        if len(jewels) < length and right < len(gems):
            jewel = gems[right]
            if jewel in jewels:
                jewels[jewel] += 1
            else:
                jewels[jewel] = 1

            right += 1

        else:
            if len(jewels) == length:
                answer.append([left, right])
            jewel = gems[left]
            jewels[jewel] -= 1
            if jewels[jewel] == 0:
                del jewels[jewel]
            left += 1

    answer.sort(key = lambda x : (x[1]-x[0], x[0]))
    if not answer:
        return [1, len(gems)]
    else:
        ans = answer[0]
        return [ans[0]+1, ans[1]]