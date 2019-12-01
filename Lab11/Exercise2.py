def create_list(l: list, i: int):
    l.append(i)
    if i > 0:
        create_list(l, i - 1)


if __name__ == '__main__':
    l = []
    n = int(input('Enter a number: '))
    create_list(l, n - 1)
    print(l)
