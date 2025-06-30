def singleNumber(nums):
    result = 0
    for num in nums:
        result ^= num
    return result

nums = [1, 3, 5, 7, 9, 1, 3, 7, 9]
print(singleNumber(nums))
