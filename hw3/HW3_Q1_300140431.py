def count_pos(l):
    positive = 0

    for i in l:
        if i > 0:
            positive += 1
    return positive


l = [float(i) for i in input(
    'Please input a list of numbers separated by space: ').split(' ')]

print(f'There are {count_pos(l)} positive numbers in your list.')
