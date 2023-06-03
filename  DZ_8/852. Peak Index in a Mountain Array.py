class Solution:

    def bool_api(self, arr, mid):

        if arr[mid] > arr[mid + 1]:
            return True
        else:
            return False

    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        lo = 0
        hi = len(arr) - 1

        while lo < hi:
            mid = (lo + hi) // 2
            if self.bool_api(arr, mid) < True:
                lo = mid + 1
            else:
                hi = mid
        return lo

    # https://leetcode.com/problems/peak-index-in-a-mountain-array/description/
