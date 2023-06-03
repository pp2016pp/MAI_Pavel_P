class Solution:
    def bool_api(self, piles, mid, h):
        time = 0

        for pile in piles:
            time += math.ceil(pile / mid)

        if time > h:
            return False
        else:
            return True

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo = 1
        hi = max(piles)
        while lo < hi:
            mid = (lo + hi) // 2
            if self.bool_api(piles, mid, h) < True:
                lo = mid + 1
            else:
                hi = mid

        return lo

    # https://leetcode.com/problems/koko-eating-bananas/
