t = (1,2,-3,3,4,-3,3,3)

def histo_n(t):
    result = {}
    for i in t:
        result[i] = result.get(i, 0) + 1
    result = list(result.items())
    result.sort()
    return result

print(histo_n(t))
