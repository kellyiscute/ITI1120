def longest_run(l: list):
    longest = 0
    for i in range(l.__len__()):
        current = 0
        for j in range(i, l.__len__()):
            if l[i] == l[j]:
                current += 1
            else:
                break
        if current > longest:
            longest = current
    return longest


usr_input = input(
    'Please input a list of numbers separated by space: ')
l = [float(i) for i in usr_input.strip().split()]
print(longest_run(l))
