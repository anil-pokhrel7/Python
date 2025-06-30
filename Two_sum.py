nums = [2, 7, 11, 15, 17]
target = 22
for i in range(0,len(nums)):
    for j in range(0, 5):
        if nums[i] != nums[j]:
            result = nums[i]+nums[j]
            if result == target:
                print(f'sum of {nums[i]} and {nums[j]} meets the target 22.')
