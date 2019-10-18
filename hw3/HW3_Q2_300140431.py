def two_length_run(l: list):
    for i in range(l.__len__()):
        for j in range(i + 1, l.__len__()):
            if l[i] == l[j]:
                return True
    return False


l = [float(i) for i in input(
    'Please input a list of numbers separated by space: ').split(' ')]
print(two_length_run(l))
