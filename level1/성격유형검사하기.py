#version1
def solution(survey, choices):
    scores = {
        'R' : 0, 'T' : 0,
        'C' : 0, 'F' : 0,
        'J' : 0, 'M' : 0,
        'A' : 0, 'N' : 0
    }
    
    # count scores for each types
    for types, answer in zip(survey,choices):
        if answer <= 3:
            scores[types[0]] += (4 - answer)
        elif answer >= 5:
            scores[types[1]] += (answer - 4)
        else:
            continue
    
    # return answers
    scores_key = list(scores.keys())
    scores_val = list(scores.values())
    
    answer = ''
    for i in range(4):
        if scores_val[2*i] > scores_val[2*i + 1]:
            answer += (scores_key[2*i])
        elif scores_val[2*i] < scores_val[2*i + 1]:
            answer += (scores_key[2*i + 1])
        else:
            answer += min(scores_key[2*i], scores_key[2*i +1])
            
    return answer