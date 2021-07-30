# version 1 (my solution)
def mid_digit_dist(mid_num, nums):
    if mid_num == nums:
        return 0
    elif mid_num == 2:
        if nums in [1, 3, 5]:
            return 1
        elif nums in [4, 6, 8]:
            return 2
        elif nums in [0, 7, 9]:
            return 3
        else:
            return 4
    elif mid_num == 5:
        if nums in [2, 4, 6, 8]:
            return 1
        elif nums in [0, 1, 3, 7, 9]:
            return 2
        else:
            return 3
    elif mid_num == 8:
        if nums in [0, 5, 7, 9]:
            return 1
        elif nums in [2, 4, 6, '*', '#']:
            return 2
        else:
            return 3
    else:
        if nums in [8, '*', '#']:
            return 1
        elif nums in [5, 7, 9]:
            return 2
        elif nums in [2, 4, 6]:
            return 3
        else:
            return 4
        
        
        

def solution(numbers, hand):
    answer = ''
    L_hand = '*'
    R_hand = '#'
    for val in numbers:
        if val in [1, 4, 7]:
            L_hand = val
            answer += 'L'
        elif val in [3, 6, 9]:
            R_hand = val
            answer += 'R'
        else:
            if mid_digit_dist(val, L_hand) < mid_digit_dist(val, R_hand):
                L_hand = val
                answer += 'L'
            elif mid_digit_dist(val, L_hand) > mid_digit_dist(val, R_hand):
                R_hand = val
                answer += 'R'
            else:
                if hand == 'left':
                    L_hand = val
                    answer += 'L'
                else:
                    R_hand = val
                    answer += 'R'
            
    return answer

# version 2 (better solution)
# 각 숫자별 좌표를 생성해준다
num_point = {
    1:(0,0), 2:(1,0), 3:(2,0),
    4:(0,1), 5:(1,1), 6:(2,1),
    7:(0,2), 8:(1,2), 9:(2,2),
    '*':(0,3), 0:(1,3), '#':(2,3)
}

# 가운데 숫자들을 누르기 위한 거리 함수 생성
def mid_digit_dist(mid_num, nums):
    return sum(abs(x - y) for x, y in zip(num_point[mid_num], num_point[nums]))
               

def solution(numbers, hand):
    answer = ''
    L_hand = '*'
    R_hand = '#'
    for val in numbers:
        if val in [1, 4, 7]:
            L_hand = val
            answer += 'L'
        elif val in [3, 6, 9]:
            R_hand = val
            answer += 'R'
        else:
        	# 가운데 숫자들을 눌러줄 때 거리 비교
            if mid_digit_dist(val, L_hand) < mid_digit_dist(val, R_hand):
                L_hand = val
                answer += 'L'
            elif mid_digit_dist(val, L_hand) > mid_digit_dist(val, R_hand):
                R_hand = val
                answer += 'R'            
            # 왼손과 오른손의 거리가 같으면 주로 사용하는 손 이용
            else:
                if hand == 'left':
                    L_hand = val
                    answer += 'L'
                else:
                    R_hand = val
                    answer += 'R'
            
    return answer
