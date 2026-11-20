def solution(numbers):
    return [((val ^ (val + 1)) >> 2) + val + 1 for val in numbers]
