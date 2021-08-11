# version 1
up_alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
low_alpha = 'abcdefghijklmnopqrstuvwxyz'

def solution(s, n):
    answer = ''
    for i in s:
        if i.isupper():
            answer += up_alpha[(up_alpha.index(i) + n)%26]
        
        elif i.islower():
            answer += low_alpha[(low_alpha.index(i) + n)%26]
            
        else:
            answer += i
        
    return answer
  
# version 2
def solution(s, n):
    s = list(s)
    
    for i, k in enumerate(s):
    	if k.isupper():
        	s[i] = chr((ord(k) - ord('A') + n) % 26 + ord('A'))
        elif k.islower():
        	s[i] = chr((ord(k) - ord('a') + n) % 26 + ord('a'))
            
    return "".join(s)
