def binary_search(l: list, c):
    t = l.copy()
    step_counter = 0
    while t.__len__() != 1:
        step_counter += 1

        middle = t.__len__() // 2
        if t[middle] == c:
            print(f'Number of steps: {step_counter}')
            print(True)
            return
        if t[middle] < c:
            t = t[middle:]
        else:
            t = t[:middle]

    print(f'Number of steps: {step_counter}')
    print(False)


if __name__ == "__main__":
    binary_search([1, 2, 3, 4, 4, 5, 7, 9, 10, 13], 6)
