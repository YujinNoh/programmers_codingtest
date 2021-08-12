# version 1
def solution(n):
    answer = []
    while(n > 0):
        answer.append(n%10)
        n = n//10
    return answer
  
# version 2
def solution(n):
    answer = []
    for i in str(n):
        answer.append(int(i))
    answer.reverse()
    return answer
