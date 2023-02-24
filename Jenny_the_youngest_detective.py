def missing(nums, s):
    nums = sorted(nums)
    res = ''
    s = s.replace(" ", "").lower()
    for i in range(len(nums)):
        if nums[i] > len(s):
            return "No mission today"
        res += s[nums[i]]
    return res