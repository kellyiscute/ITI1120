def sum_matrixex(m, n):
    for i in range(len(m)):
        for j in range(len(m[0])):
            m[i][j] += n[i][j]
    return m


def enter_matrix():
    m = []
    t = []
    while t.__len__() != 0 or m.__len__() == 0:
        t = [int(i) for i in input(
            'Enter next row, leave empty to end: ').strip().split()]
        if t.__len__() != 0:
            m.append(t)
    return m


if __name__ == "__main__":
    print('Enter the first matrix')
    m = enter_matrix()
    print('Enter the second matrix')
    n = enter_matrix()
    print(sum_matrixex(m, n))
    # print(sum_matrixex([[1, 2], [3, 4]], [[1, 1], [1, 1]]))
