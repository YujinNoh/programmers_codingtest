def solution(price, money, count):
    return 0 if sum(range(1, count + 1)) * price <= money else sum(range(1, count + 1)) * price - money
