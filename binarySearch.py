def search(nums, target):
    l, r = 0, len(nums) - 1

    2^31
    while l <= r:
        m = (l + r) // 2
        if nums[m] > target:
            r = m - 1
        elif nums[m] < target:
            l = m + 1
        else:
            return m
    return -1 #did not find a result
print(search([1,2,3,4,5], 4))