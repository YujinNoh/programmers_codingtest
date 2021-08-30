class Solution:
    def romanToInt(self, s: str) -> int:
        answer = 0
        Roman = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000,
        }
        
        for i, val in enumerate(s):
            if val in ('I','X','C'):
                if i < len(s)-1:
                    if Roman[val] < Roman[s[i+1]]:
                        answer -= 2 * Roman[val]
            answer += Roman[val]
        return answer
