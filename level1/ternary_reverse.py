# version 1
def ToTernary(num):
    result = 0
    pow = 0
    base = 1
    while True:
        k = num // base
        if k >= 3:
            base *= 3
            pow += 1
            
        elif k >= 1 and k <= 2 :
            result += (k * (10 ** (pow)))
            num -= (base * k)
            base = 1
            pow = 0
            
        else:
            break
        
    return result
    
def solution(n):
    answer = ''
    ternary = ToTernary(n)
    
    while ternary > 0:
        answer += str(ternary % 10) 
        ternary = ternary // 10

    return int(answer, 3)

  
# version 2 (shortest version)
def solution(n):
    answer = ''
    
    while n:
        answer += str(n % 3)
        n = n // 3

    return int(answer, 3)
