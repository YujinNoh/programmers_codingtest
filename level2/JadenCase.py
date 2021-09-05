def solution(s):
    for i, k in enumerate(s.split(" ")):
        if len(k) >= 2:
            words[i] = k[0].upper() + k[1:].lower()
        else:
            words[i] = k.upper()
    return " ".join(words)
