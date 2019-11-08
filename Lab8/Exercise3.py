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


if __name__ == "__main__":
    print(product_matrixes([[1, 2, 3], [4, 5, 6]], [[1, 2], [3, 4], [5, 6]]))
