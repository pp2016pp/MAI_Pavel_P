# https://leetcode.com/problems/binary-search/description/
from bisect import bisect_left

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        ans = bisect_left(nums, target, 0, len(nums) - 1)
        if nums[ans] != target:
            return -1
        else:
            return ans