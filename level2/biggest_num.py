def solution(numbers):
    numbers = [str(x) for x in numbers]
    list_max = sorted(numbers, key = lambda x : (x * 4)[:4], reverse = True)
    
    if list_max[0] == "0":
        return "0"
    else:
        return "".join(list_max)
