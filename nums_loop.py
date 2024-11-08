nums = [2,7,11,15]
target = 9
g = len(nums)
for i in range(0, g): #0
    for an_one in range(i+1, g): #0
        v = nums[i] + nums[an_one]
        if v == target:
              return [i, an_one]
