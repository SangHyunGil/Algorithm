import math

def solution(n, words):
    answer = []
    
    check = set()
    for i in range(1, len(words)):
        if words[i] in check or (words[i-1][-1] != words[i][0]):
            return [i%n, math.ceil(i/n)]

        check.add(words[i])

    return [0, 0]

solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"])
solution(5, ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"])