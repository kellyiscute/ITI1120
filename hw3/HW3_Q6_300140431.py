def roman_v1(s: str):
    result = 0
    result += s.count('M') * 1000
    result += s.count('D') * 500
    result += s.count('C') * 100
    result += s.count('X') * 10
    result += s.count('V') * 5
    result += s.count('I') * 1

    return result


def roman_v2(s):
    result = 0
    for i in range(s.__len__()):
        if s[i] == 'M':
            result += 1000
        elif s[i] == 'D':
            result += 500
        elif s[i] == 'C':
            result += 100
        elif s[i] == 'X':
            result += 10
        elif s[i] == 'V':
            result += 5
        elif s[i] == 'I':
            result += 1

    return result


s = input('Input a roman number using the letters M, D, C, X and I: ').strip()
print(roman_v1(s))
print(roman_v2(s))
