# version 1
def solution(arr):
    answer = []
    for i, val in enumerate(arr):
        if i == 0:
            answer.append(val)
        elif val == answer[-1]:
            continue
        else:
            answer.append(val)
    return answer
