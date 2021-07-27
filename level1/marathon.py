# version 1 O(n^3)
def solution(participant, completion):
	for x in participant:
      if x in completion:
        	participant.remove(x)
            
    return participant[0]
# version 2 O(n^2)
def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i, val in enumerate(participant):
        if i == (len(participant)-1):
            return val
        if val != completion[i]:
            return val
