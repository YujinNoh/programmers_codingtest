# version 1 (my solution)
from math import ceil, floor

def solution(w,h):
    cut = 0
    height = max(w,h)
    width = min(w,h)
    if w == 1 or h == 1:
        return 0
    elif w == h:
        return w * h - w
    else:
        for i in range(0, width):
            cut += ceil(height * (i + 1) / width) - floor((height * i)/ width)
        return w * h - cut
      
# version 2 (other solution)
from math import gcd
def solution(w,h): return w * h - w - h + gcd(w,h)
