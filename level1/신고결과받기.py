#version1
def solution(id_list, report, k):
    answer = []
    
    dict = {}
    reported = {}
    for i in id_list:
        dict[i] = []
        reported[i] = 0
    
    # 한 유저가 같은 유저를 여러번 신고한 경우 제거
    report = list(set(report))
    
    # 유저별 신고한 사람, 신고당한 횟수 정리
    for i in report:
        er, ee = i.split(" ")
        dict[er] = dict.get(er) + [ee]
        reported[ee] += 1

    
    # 정지당한 id 리스트
    reported_id = []
    for i, count in zip(reported.keys(), reported.values()):
        if count >= k:
            reported_id.append(i)

    # 메일 받는 횟수
    for r in dict.values():
        mail = 0
        for i in r:
            if i in reported_id:
                mail += 1
        answer.append(mail)
    

    return answer

#version2
def solution(id_list, report, k):
    answer = [0] * len(id_list)
    reported = {i:0 for i in id_list}

    for i in set(report):
        reported[i.split(" ")[1]] += 1

    
    for i in set(report):
        if reported[i.split(" ")[1]] >= k:
            answer[id_list.index(i.split(" ")[0])] += 1
        
    
    return answer