import numpy as np

def solution(scores):
    answer = ''
    scores = np.array(scores)
    self_score = np.diag(scores)

    print(self_score)

    for i, val in enumerate(self_score):
        if val == np.max(scores[:,i]):
            if len(np.where(scores[:,i] == val)[0]) == 1:
                scores[i,i] = 0
        elif val == np.min(scores[:,i]):
            if len(np.where(scores[:,i] == val)[0]) == 1:
                scores[i,i] = 0

    score_mean = np.true_divide(scores.sum(0), (scores!=0).sum(0))
    
    for val in score_mean:
        if val >= 90:
            answer += 'A'
        elif val >= 80:
            answer += 'B'
        elif val >= 70:
            answer += 'C'
        elif val >= 50:
            answer += 'D'
        else:
            answer += 'F'

    return answer
