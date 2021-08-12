# version 1
def solution(s):
    answer = ''
    
    for word in s.split(' '):
        for i, k in enumerate(word):
            if i % 2 == 0:
                answer += k.upper()
            else:
                answer += k.lower()
        answer += ' '
             
    return answer[:-1]
