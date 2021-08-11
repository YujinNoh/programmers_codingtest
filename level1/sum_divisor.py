def solution(n):
    answer = 1
    
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            answer += i
            if i != (n // i):
                answer += (n // i)
                
    return n if n <=1 else answer + n
