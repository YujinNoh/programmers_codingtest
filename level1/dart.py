# version 1 
import re

def solution(dartResult):
    num_stack= []
    idx = 0

    p1 = re.compile('[0-9]*')
    for num in p1.findall(dartResult):
        if num :
            num_stack.append(int(num))
    
    p2 = re.compile('[SDT*#]')
    for others in p2.findall(dartResult):
        if others in "SDT":
            if others == "S":
                pass
            elif others == 'D':
                num_stack[idx] = num_stack[idx] ** 2
            else:
                num_stack[idx] = num_stack[idx] ** 3
        
        if others in "#*":
            idx -= 1
            if others == "#":
                num_stack[idx] *= -1
            
            else:
                num_stack[idx] *= 2
                if idx >= 1:
                    num_stack[idx-1] *=2
        idx += 1 
    
    return sum(num_stack)
  
# version 2 (other solution)
import re

def solution(dartResult):
    bonus = {'S' : 1, 'D' : 2, 'T' : 3}
    option = {'' : 1, '*' : 2, '#' : -1}
    
    p = re.compile('(\d+)([SDT])([*#]?)') # (점수, 보너스, 옵션)의 튜플을 원소로 가지는 리스트가 만들어짐
    dart = p.findall(dartResult)
    print(dart)
    
    for i in range(len(dart)):
        if dart[i][2] == '*' and i > 0:
            dart[i-1] *= 2
        dart[i] = int(dart[i][0]) ** bonus[dart[i][1]] * option[dart[i][2]]

    return sum(dart)
