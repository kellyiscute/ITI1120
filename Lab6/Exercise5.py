def spaces(s):
    result = ''
    for i in s:
        result += i
        result += ' '
    return result.strip()

if __name__ == "__main__":
    s = input('Enter a string: ')
    print(spaces(s))
