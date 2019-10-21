def longest_run(l: list):
    longest = 0
    current = 1
    for i in range(1, l.__len__()):
        if l[i] == l[i - 1]:
            current += 1
            if current > longest:
                longest = current
        else:
            current = 1
    return longest


usr_input = input(
    'Please input a list of numbers separated by space: ')
l = [float(i) for i in usr_input.strip().split()]
print(longest_run(l))
