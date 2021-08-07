# version 1
def solution(s):
    s = s.lower()
    p = s.count('p')
    y = s.count('y')
    
    return True if p == y else False
  
# version 2
def solution(s):
    s = s.lower()
    return True if s.count('p') == s.count('y')
