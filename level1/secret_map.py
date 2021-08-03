# version 1
def n_bin(num, n):
    answer = []
    while num:
        answer.append(num % 2)
        num = num // 2
    if len(answer) < n:
        answer = answer + [0] * (n - len(answer)) 
    return reversed(answer)

def solution(n, arr1, arr2):
    answer = []
    for a, b in zip(arr1, arr2):
        row = ""
        for x, y in zip(n_bin(a, n), n_bin(b, n)):
            if (x or y) == 1:
                row += "#"
            else:
                row += " "
        answer.append(row)
        
    return answer
  
# version 2
def solution(n, arr1, arr2):
	answer = []
    for i, j in zip(arr1, arr2):
    	row = str(bin(i|j)[2:])
        row = row.rjust(n, '0')  # n 길이가 될 수 있게 문자열 앞부분에 0을 채워넣어라
        row = row.replace('0', ' ').replace('1', '#')
    	answer.append(row)
    return answer
