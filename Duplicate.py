def containsDuplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False
    
my_list = [10, 20, 30, 40, 50, 30]
print(containsDuplicate(my_list))