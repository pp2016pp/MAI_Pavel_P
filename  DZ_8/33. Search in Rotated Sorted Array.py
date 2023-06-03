class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo = 0
        hi = len(nums) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] > nums[hi]:
                lo = mid + 1
            else:
                hi = mid
        point = lo
        if target >= nums[point] and target <= nums[-1]:
            lo = point
            hi = len(nums) - 1
        else:
            lo = 0
            hi = point - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return -1

    # https://leetcode.com/problems/search-in-rotated-sorted-array/
