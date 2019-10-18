import math


def calc_average(nums):
    sum = 0
    for i in nums:
        sum += i
    return sum / len(nums)


def calc_standard_deviation(l):
    a = calc_average(l)
    numerator = 0
    for i in l:
        numerator += (i - a) ** 2
    return math.sqrt(numerator) / len(l)


l = eval(input('Enter a list: '))
print(f'The standard deviations is: {calc_standard_deviation(l)}')
