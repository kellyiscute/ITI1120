def revd(s):
    result = ''
    for i in range(s.__len__() - 1, -1, -1):
        result += s[i] * 2
    return result


s = input('Please enter a chain of chareters: ')
print(revd(s))
