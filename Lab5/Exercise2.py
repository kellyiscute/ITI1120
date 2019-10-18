def calc_average(nums):
    sum = 0
    for i in nums:
        sum += i
    return sum / len(nums)

def maximum(nums):
    max = nums[0]
    for i in nums:
        if i > max:
            max = i
    return max

def minimum(nums):
    min = nums[0]
    for i in nums:
        if i < min:
            min = i
    return min

l = eval(input('Input a list of student\'s mark: '))
print([calc_average(l), maximum(l), minimum(l)])
