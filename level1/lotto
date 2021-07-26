# version 1 (initial answer)
def solution(lottos, win_nums):
    min, max = 0, 0
    zeros = 0
    match = 0
    for lot_num in lottos:
        for win_num in win_nums:
            if lot_num == 0:
                zeros += 1
                break
            if lot_num == win_num:
                match += 1
    
    min = 7 - match if match >= 2 else 6
    max = 7 - (match + zeros) if (match + zeros) >= 2 else 6
    
    return [max, min]
    

# version 2 (revised answer)
def solution(lottos, win_nums):
    min, max = 0, 0
    zeros = lottos.count(0)
    match = 0
    for lot_num in lottos:
        if lot_num in win_nums:
            match += 1
    
    min = 7 - match if match >= 2 else 6
    max = 7 - (match + zeros) if (match + zeros) >= 2 else 6
    
    return [max, min]
