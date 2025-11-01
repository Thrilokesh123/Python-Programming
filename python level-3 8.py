nums = [5,7,7,8,8,10]
target = 8

if target in nums:
    first = nums.index(target)
    last = len(nums) - 1 - nums[::-1].index(target)
    print([first, last])
else:
    print([-1, -1])