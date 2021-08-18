def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)    

def solution(n, m):
    GCD = gcd(n, m)
    LCM = n * m / GCD
    return [GCD, LCM]
