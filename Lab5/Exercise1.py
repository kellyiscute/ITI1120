def calc_average(nums: list) -> int:
    sum = 0
    for i in nums:
        sum += i
    return sum / len(nums)


l = eval(input('Input a list of number: '))
print(calc_average(l))
