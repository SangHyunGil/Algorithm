from collections import defaultdict

def solution(lottos, win_nums):

    ans = 0

    orders = [6, 6, 5, 4, 3, 2, 1]

    temp = defaultdict(list)

    

    for i in range(46):

        temp[i] = 0

    for l in lottos:

        temp[l] += 1

        

    for w in win_nums:

        if temp[w]:

            ans += 1

            

    answer = [orders[ans+temp[0]], orders[ans]]

 

    return answer