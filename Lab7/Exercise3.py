def sum_of_three(x):
    '''(tuple)->bool
    Returns True if the sum of 3 consecutive
    elements is zero
    Precondition: the tuple has at least 3
    elements
    >>> t = (1,2,-3,4,-1,3)
    >>> sum_of_three(t)
    True
    '''
    for i in range(len(x) - 2):
        if x[i] + x[i + 1] + x[i + 2] == 0:
            return True
    return False

t = (1,2,-3,4,-1,3)
print(sum_of_three(t))
