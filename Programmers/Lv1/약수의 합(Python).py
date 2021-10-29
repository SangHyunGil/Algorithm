def solution(s):
    answer = []
    s = s.split(" ")
    print(s)
    for word in s:
        temp = []
        for idx, w in enumerate(word):
            if idx % 2 == 0:
                temp.append(w.upper())
            else:
                temp.append(w.lower())
        answer.append("".join(temp))

    return " ".join(answer)

print(solution("hel    odfs"))