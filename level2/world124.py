# version 1
def solution(n):
    answer = ''
    while n :
        num = n % 3 
        if num == 1:
            ans = '1'
        elif num == 2:
            ans = '2'
        else:
            ans = '4'
            n -= 1
        answer = ans + answer
        n = n // 3
    return answer
  
# version 2
def solution(n):
    answer = ''
    num124 = ['1','2','4']
    while n:
        n -= 1
        answer = num124[n % 3] + answer
        n = n // 3
    return answer
