# version 1 (my solution)
def solution(array, commands):
    answer = []
    for val in commands:
        i, j, k = val
        arr = array[i-1:j]
        arr.sort()
        answer.append(arr[k-1])
    return answer

# version 2 (shortest solution)
def solution(array, commands):
    return list(map(lambda x : sorted(array[x[0]-1: x[1]])[x[2]-1], commands))
