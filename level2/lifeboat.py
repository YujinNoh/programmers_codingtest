def solution(people, limit):
    answer = 0
    if len(people) == 1:
        return 1
    else:
        people = sorted(people)
        
        left = 0
        right = len(people) - 1
        while (left < right):
            if people[left] <= (limit - people[right]):
                left += 1
            right -= 1
            answer += 1
        return answer + 1 if left == right else answer
