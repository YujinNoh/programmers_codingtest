# version 1 (my solution)
def solution(s):
    answer = ''
    temp = ''
    nums = {
        'zero' : 0,
        'one' : 1,
        'two' : 2,
        'three' : 3,
        'four' : 4,
        'five' : 5,
        'six' : 6,
        'seven' : 7,
        'eight' : 8,
        'nine': 9
    }
    
    for x in s:
        if x in '0123456789':
            answer += x
        else:
            temp += x
            if temp in nums.keys():
                answer += str(nums[temp])
                temp = ''
    return int(answer)

  # version 2 (other approach)
  def solution(s):
    
    nums = {
        'zero' : 0,
        'one' : 1,
        'two' : 2,
        'three' : 3,
        'four' : 4,
        'five' : 5,
        'six' : 6,
        'seven' : 7,
        'eight' : 8,
        'nine': 9
    }
    
    for num in nums:
        s = s.replace(num, str(nums.get(num)))

    return int(s)
