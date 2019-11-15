def insertion_sort(l):
    for i in range(1, l.__len__()):
        j = i
        t = l[i]
        while j > 0 and t < l[j-1]:
            j -= 1
        del l[i]
        l.insert(j, t)
    return l


if __name__ == "__main__":
    print(insertion_sort([3, 4, -1, 7, 2, 5, 16, -2, 17, 7, 82, -1]))
