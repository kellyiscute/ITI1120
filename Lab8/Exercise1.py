def transpose(l):
    result = []
    for i in range(l[0].__len__()):
        t = []
        for j in range(l.__len__()):
            t.append(l[j][i])
        result.append(t)
    return result


if __name__ == "__main__":
    m = []
    t = []
    while t.__len__() != 0 or m.__len__() == 0:
        t = [int(i) for i in input(
            'Enter next row, leave empty to end: ').strip().split()]
        if t.__len__() != 0:
            m.append(t)
    print(transpose(m))
