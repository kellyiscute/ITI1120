def stars(num: int):
    if num > 1:
        print('*' * num)
        stars(num - 1)
    print('*')


def sumListPos_rec(l: list, i: int):
    if i == 1:
        if l[i - 1]>0:
            return l[i - 1]
        else:
            return 0
    else:
        if l[i - 1] > 0:
            return l[i - 1] + sumListPos_rec(l, i - 2)
        else:
            return sumListPos_rec(l, i - 2)
