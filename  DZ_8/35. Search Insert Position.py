from bisect import bisect_left


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        ans = bisect_left(nums, target, 0, len(nums) - 1)
        if ans == len(nums) - 1:
            if target <= nums[ans]:
                return ans
            else:
                return ans + 1
        else:
            return ans

        # https://leetcode.com/problems/search-insert-position/
