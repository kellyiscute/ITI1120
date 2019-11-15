def find_m(m, c):
    counter = 0
    for i in m:
        for j in i:
            counter += 1
            if j == c:
                print(f'Number of steps: {counter}')
                print(True)
                return
    print(f'Number of steps: {counter}')
    print(False)
