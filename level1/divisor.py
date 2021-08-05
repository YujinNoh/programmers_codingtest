# version 1 (my solution)

def solution(arr, divisor):
    answer = []
    for val in arr:
        if val % divisor == 0:
            answer.append(val)
    
    if len(answer) == 0:
        answer.append(-1)
    
    print(arr[arr % divisor == 0])
    
    return sorted(answer)
  
  
# version 2 (other solution)
def solution(arr, divisor): 
	return sorted([n for n in arr if n % divisor == 0]) or [-1]
