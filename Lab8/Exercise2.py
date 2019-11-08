def sum_matrixex(m, n):
    for i in range(len(m)):
        for j in range(len(m[0])):
            m[i][j] += n[i][j]
    return m


if __name__ == "__main__":
    print(sum_matrixex([[1, 2], [3, 4]], [[1, 1], [1, 1]]))
