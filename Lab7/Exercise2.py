def histo_n(t):
    result = {}
    for i in t:
        result[i] = result.get(i, 0) + 1
    result = list(result.items())
    result.sort()
    return result
