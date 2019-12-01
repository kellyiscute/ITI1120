def bcd(x: int, y: int):
    if x >= y and x % y == 0:
        return y
    elif x < y:
        return bcd(y, x)
    else:
        return bcd(y, x % y)


if __name__ == '__main__':
    print(bcd(1234, 4321))
    print(bcd(8192, 192))
