def two_length_run(l: list):
    for i in range(l.__len__()-1):
        if l[i] == l[i+1]:
            return True
    return False


l = [float(i) for i in input(
    'Please input a list of numbers separated by space: ').strip().split()]
print(two_length_run(l))
