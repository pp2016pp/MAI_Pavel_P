class Solution:
    def bool_api(self, nums, mid):
        if nums[mid] > nums[mid + 1]:
            return True
        else:
            return False

    def findPeakElement(self, nums: List[int]) -> int:

        lo = 0
        hi = len(nums) - 1

        while lo < hi:

            mid = (lo + hi) // 2

            if self.bool_api(nums, mid) < True:
                lo = mid + 1
            else:
                hi = mid

        return lo

    # https://leetcode.com/problems/find-peak-element/
