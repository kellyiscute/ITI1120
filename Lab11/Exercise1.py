def check_integer(l: list, i: int):
    if i > 0:
        return l[i] in range(10) and check_integer(l, i-1)
    else:
        return l[i] in range(10)


if __name__ == '__main__':
    l = [1,2,4,6,4]
    print(check_integer(l, len(l)-1))
