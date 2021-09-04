def solution(brown, yellow):
    for h in range(1, 5000):
        if (brown + yellow) % h == 0:
            w = (brown + yellow) / h
            if (w - 2) * (h - 2) == yellow:
                return [w, h]
