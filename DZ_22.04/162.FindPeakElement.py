class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        def binary_search(nums, left, right):
            if left == right:
                return left
            mid = (left + right) // 2
            if nums[mid] > nums[mid+1]:
                return binary_search(nums, left, mid)
            else:
                return binary_search(nums, mid+1, right)
        return binary_search(nums, 0, len(nums)-1)