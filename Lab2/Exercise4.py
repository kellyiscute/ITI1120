def numRealRoot(a, b, c):
    delta = b ** 2 - 4 * a * c
    if delta == 0:
        return 1
    elif delta == 1:
        return 2
    else:
        return 0

if __name__ == "__main__":
    a = float(input('Enter a: '))
    b = float(input('Enter b: '))
    c = float(input('Enter c: '))
    
    print('This quadratic has', numRealRoot(a,b,c), 'real roots')