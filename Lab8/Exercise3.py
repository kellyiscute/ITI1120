def product_matrixes(m, n):
    result = []
    for i in range(m.__len__()):
        t = []
        for j in range(n[0].__len__()):
            num = 0
            for k in range(m[0].__len__()):
                num += m[i][k] * n[k][j]
            t.append(num)
        result.append(t)
    return result


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
    print(product_matrixes(m, n))
    # print(product_matrixes([[1, 2, 3], [4, 5, 6]], [[1, 2], [3, 4], [5, 6]]))
