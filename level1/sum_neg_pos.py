# version 1 (my solution)
def solution(absolutes, signs):
    sign = list(map((lambda x: 1 if x else -1), signs))
    return sum([a*b for a, b in zip(absolutes, sign)])

# version 2 (shortest solution)
def solution(absolutes, signs):
    return sum(absolutes if sign else -1 * absolutes for absolutes, sign in zip(absolutes, signs))
