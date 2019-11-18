def add(l: list) -> None:
    """
    (list)->None
    add 1 to every element in an array
    """
    for row in range(l.__len__()):
        for col in range(l[row].__len__()):
            l[row][col] = l[row][col] + 1


def add_v2(l: list) -> list:
    """
    (list)->list
    takes an array and
    returns a new array containing the values of the given array provided as a parameter incremented by 1,
    without modifying it
    """
    result = []
    for row in range(l.__len__()):
        t = []
        for col in range(l[row].__len__()):
            t.append(l[row][col] + 1)
        result.append(t)
    return result


def enter_matrix():
    """
    ()->list
    method to input an array
    """
    m = []
    t = []
    while t.__len__() != 0 or m.__len__() == 0:
        t = [int(i) for i in input(
            '').strip().split()]
        if t.__len__() != 0:
            m.append(t)
    return m


if __name__ == '__main__':
    print('Input the array elements with spaces between columns.\nOne row per line, and an empty line at the end.')
    m = enter_matrix()
    print(f'The array is:\n{m}')
    add(m)
    print(f'After executing the function add, the array is:\n{m}')
    n = add_v2(m)
    print(f'A new array created with add_V2:\n{n}')
    print(f'After executing the function add_V2, the initial array is:\n{m}')
