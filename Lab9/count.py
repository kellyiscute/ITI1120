def count(l, c):
    counter = 0
    step_counter = 0
    for i in l:
        step_counter += 1
        if i == c:
            counter += 1
    print(f'Number of steps: {step_counter}')
