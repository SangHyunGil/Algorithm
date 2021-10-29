def solution(s):
    answer = []
    # 공백 분리
    s = s.split(" ")
    for word in s:
        # 단어 변형
        temp = []
        for idx, w in enumerate(word):
            if idx % 2 == 0:
                temp.append(w.upper())
            else:
                temp.append(w.lower())
        answer.append("".join(temp))

    return " ".join(answer)

print(solution("hel    odfs"))