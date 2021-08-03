def solution(d, budget):
    d.sort()
    result = 0
    for cost in d:
        if budget >= cost:
            budget -= cost
            result += 1
    return result
