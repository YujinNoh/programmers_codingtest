# version 1 (my solution)
def solution(board, moves):
    answer = 0
    num_pop = 0
    bag = []
    
    for i in moves:
        for row in board:
            if row[i-1] == 0:
                continue
            else:
                bag.append(row[i-1])
                row[i-1] = 0
                break
        
        # 만약 bag의 마지막 두 숫자가 같으면 pop
        if len(bag) >= 2 and bag[-1] == bag[-2]:
            bag.pop()
            bag.pop()
            num_pop += 2
                       
    return num_pop
