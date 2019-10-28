def get_histo(s):
    result = {}
    for i in s:
        result[i] = result.get(i, 0) + 1

    result = list(result.items())
    result.sort()
    return result


print(get_histo(input('Enter a string: ')))
