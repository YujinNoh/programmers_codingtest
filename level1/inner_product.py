# version 1 (my solution)
def solution(a, b):
    answer = 0
    for i, val in enumerate(a):
        answer += (val * b[i])
    return answer
  
# version 2 (shortest version)
def solution(a, b):
	return sum([x*y for x, y, in zip(a, b)])
