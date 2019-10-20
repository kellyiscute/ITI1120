def computeFact(n):
    if n == 0:
        return 1

    result = 0
    for i in range(1, n + 1):
        result *= i
    return result


while True:
    n = int(input('Enter a positive number: '))
    if n >= 0:
        print('You have entered a negative number! Please try again')
print(computeFact(n))
