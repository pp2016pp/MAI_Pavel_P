class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        left = 1
        right = sum(candies)
        while left < right:
            mid = left + (right - left) // 2
            num_children = self.get_num_children(candies, mid)
            if num_children >= k:
                left = mid + 1
            else:
                right = mid
        return left - 1

    def get_num_children(self, candies, max_per_child):
        num_children = 0
        for candy in candies:
            num_children += candy // max_per_child
        return num_children