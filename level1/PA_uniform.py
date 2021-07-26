# version 1
def solution(n, lost, reserve):
    answer = n
    delete = []
    
    # 여유분이 있었지만 잃어버린 학생들 
    for i in lost:
        if i in reserve:
            delete.append(i)
            
    # 위에 해당하는 학생들은 체육복을 빌려줄 수 없으므로 삭제
    for k in delete:
        lost.remove(k)
        reserve.remove(k)
        
    # 빌릴 수 없는 학생들의 숫자를 빼는 형식으로 계산
    for l in lost:
        if (l-1 in reserve):
            reserve.remove(l-1) 
        elif (l+1 in reserve):
            reserve.remove(l+1)
        else:
            answer -= 1
           
    
    return answer
