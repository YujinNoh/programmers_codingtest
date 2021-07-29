# version 1 (my solution)
def solution(answers):
    # 학생들의 점수를 담을 리스트
    scores = [0, 0, 0]
    
    # 각 학생들의 찍는 패턴
    data1 = [1, 2, 3, 4, 5]
    data2 = [2, 1, 2, 3, 2, 4, 2, 5]
    data3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    for i, val in enumerate(answers):
        if val == data1[(i % 5)]:
            scores[0] += 1
        
        if val == data2[(i % 8)]:
            scores[1] += 1
        
        if val == data3[(i  % 10)]:
            scores[2] += 1

    # 학생들의 점수를 체크
    winner = []
    
    for idx, score in enumerate(scores):
        if score == max(scores):
            winner.append(idx+1)
            
    return winner
