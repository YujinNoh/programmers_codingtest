# my solution
def solution(citations):
    answer = 0
    temp = 0
    for h in range(1, max(citations)):
        for i in citations:
            if i >= h:
                temp += 1
        if temp >= h:
            answer = h
        temp = 0
        
    return answer

# other solution
def solution(citations):
    citations.sort(reverse=True)
    return max(map(min, enumerate(citations, start=1)))
