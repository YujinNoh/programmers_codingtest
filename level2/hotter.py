import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while (len(scoville) >= 2) and (scoville[0] < K):
        hot1 = heapq.heappop(scoville)
        hot2 = heapq.heappop(scoville)
        heapq.heappush(scoville, hot1 + 2 * hot2)
        answer += 1
    
    if scoville[0] < K:
        answer = -1
    
    return answer
