def isDivisible(i):
    by2 = i % 2 == 0
    by3 = i % 3 == 0
    if by2 and by3:
        return 1
    elif by2 or by3:
        return 2
    else:
        return 0

i = input('Enter an integer: ')
print(isDivisible(i))
