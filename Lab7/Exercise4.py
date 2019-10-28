def move_zeros_v1(l):
    new = []
    zeros = 0
    for i in l:
        if i != 0:
            new.append(i)
        else:
            zeros += 1

    new.extend([0] * zeros)


def move_zeros_v2(l):
    step_counter = 0
    pos_counter = 0
    while step_counter < len(l):
        if l[pos_counter] == 0:
            del l[pos_counter]
            l.append(0)
        else:
            pos_counter += 1
        step_counter += 1


def move_zeros_v3(l):
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            if l[i] < l[j]:
                t = l[i]
                l[i] = l[j]
                l[j] = t
