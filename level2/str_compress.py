def solution(s):
    answer = []
    if len(s) == 1:
        return 1
    else:
        for i in range(1, len(s) // 2 + 1):
            sliced = [s[k : k + i] for k in range(0, len(s), i)]
            result = ''
            repeated = 0
            for idx, k in enumerate(sliced):
                if idx == 0:
                    pass
                elif sliced[idx - 1] == k:
                    repeated += 1
                else:
                    if repeated >= 1:
                        result += (str(repeated + 1) + sliced[idx - 1])
                    else:
                        result += sliced[idx - 1]
                    repeated = 0

                if idx == len(sliced) - 1:
                    if repeated == 0:
                        result += k
                    else:
                        result += (str(repeated + 1) + k)
            answer.append(len(result))
    return min(answer)
