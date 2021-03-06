from itertools import combinations

def solution(numbers):
    answer = []
    for (a, b) in combinations(numbers, 2):
        answer.append(a + b)
    
    return list(sorted(set(answer)))
