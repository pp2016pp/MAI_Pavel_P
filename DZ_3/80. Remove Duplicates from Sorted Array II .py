class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i, count = 0, 1
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
                count = 1
            elif count < 2:
                i += 1
                nums[i] = nums[j]
                count += 1
        return i + 1

# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/