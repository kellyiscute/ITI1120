def transpose(l):
    result = []
    for i in range(l[0].__len__()):
        t = []
        for j in range(l.__len__()):
            t.append(l[j][i])
        result.append(t)
    return result


if __name__ == "__main__":
    print(transpose([[1, 2, 3], [4, 5, 6]]))
