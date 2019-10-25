def code(s):
    secret = ''
    for i in range(0, len(s), 2):
        secret += s[i + 1]
        secret += s[i]
    return secret


if __name__ == "__main__":
    s = input('Enter a secret: ')
    print(code(s))
