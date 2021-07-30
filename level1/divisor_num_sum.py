# version 1 (my solution)
def divisors(num):
    div_list = [1]
    for i in range(2, num + 1):
        if num % i == 0:
            div_list.append(i)
    
    return 1 if len(div_list) % 2 == 0 else -1

def solution(left, right):
    return sum([divisors(i) * i for i in range(left, right + 1)])

# version 2 (shortest version)
def divisors(num):
    return -num if num % (num ** 0.5) == 0 else num
    
def solution(left, right):
    return sum([divisors(i) for i in range(left, right + 1)])
