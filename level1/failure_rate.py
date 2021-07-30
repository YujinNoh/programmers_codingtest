def solution(N, stages):
    failure = {}
    answer = []
    max_stage = max(stages)
    
    for i in range(1, N + 1):
        total = 0
        unclear = stages.count(i)
        for k in stages:
            if k >= i:
                total += 1
        
        # 도달한 사람이 없을 경우 실패율은 0으로 둠
        if total == 0:
            failure[i] = 0
        else:
            failure[i] = unclear / total 
    
    # 실패율에 따른 stage 번호 append
    failure_sort = sorted(failure.items(), 
                          reverse = True, 
                          key = lambda item : item[1])

    for (key, value) in failure_sort:
        answer.append(key)

    return answer
