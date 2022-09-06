#version 1
def solution(sizes):
    width = []
    height = []
    
    for w,h in sizes:
        if w >= h:
            width.append(w)
            height.append(h)
        else:
            width.append(h)
            height.append(w)
            
    return max(width) * max(height)

#version 2
def solution(sizes):
    return max(max(x) for x in sizes) * max(min(x) for x in sizes)