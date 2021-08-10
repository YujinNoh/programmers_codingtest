def solution(n):
    answer = n-1
    for i in range(3, n + 1):
        for k in range(2, int(i ** 0.5) + 1):
            if i % k  == 0 :
                answer -= 1
                break
    return answer
