def solution(numbers):
    numbers = list(map(str, numbers))
    length = len(max(numbers, key = len))
    numbers = [(number*(length//len(number))+number[:length%len(number)], number) for number in numbers]
    numbers.sort(reverse=True)
    print(numbers)
    return "".join([number[1] for number in numbers])

print(solution([3, 30, 345, 5, 9]))
