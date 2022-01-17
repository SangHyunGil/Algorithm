def solve(arr):
    arr = sorted(arr, key=lambda x : (x[0], -x[1]))
    
    stack = [arr[0]]
    for a in arr[1:]: # O(N)
        if stack[-1][0] != a[0]:
            if stack[-1][0] < a[0] <= stack[-1][1]:
                stack[-1] = [stack[-1][0], max(stack[-1][1], a[1])]
            else:
                stack.append(a)

    answer = 0
    for s in stack: # O(N)
        answer += s[1] - s[0]
    
    print(answer)


solve([[1, 6], [1, 3], [3, 5], [8, 10], [10, 11]])