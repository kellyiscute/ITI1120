def count(s, find):
    c = 0
    for i in s:
        if i == find:
            c += 1
    return c

if __name__ == "__main__":
    s = input('Enter a string: ')
    c = input('Enter another string: ')
    print(count(s, c))
    print(s.count(c))
