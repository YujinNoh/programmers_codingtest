# version 1
def solution(n):
    answer = 0

    while(n > 0):
        answer += n % 10
        n = n // 10

    return answer

# version 2
def solution(n):
    answer = 0

    for i in str(n):
        answer += int(i)

    return answer
