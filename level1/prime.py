# version 1 (my solution)
from itertools import combinations

def solution(nums):
    combi = list(combinations(nums,3))
    answer = len(combi)
    sums = []
    for c in combi:
        for i in range(2, sum(c)+1):
            if (sum(c) % i == 0):
                if i != sum(c):
                    answer -= 1
                    break

    return answer

  
# version 2 (shortest time solution)  
from itertools import combinations

# 에라토스테네스의 체
def is_prime(n):
    divisor = 0
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            divisor += 1

    return True if divisor == 0 else False

def solution(nums):
    return [is_prime(sum(c)) for c in combinations(nums,3)].count(True)
