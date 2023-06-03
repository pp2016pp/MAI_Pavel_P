class Solution:
    def bool_api(self, ranks, cars, mid):
        time = 0
        for rank in ranks:
            time += math.floor((mid / rank) ** 0.5)
        if time < cars:
            return False
        else:
            return True
    def repairCars(self, ranks: List[int], cars: int) -> int:
        lo = 0
        hi = max(ranks) * cars * cars
        while lo < hi:
            mid = (lo + hi) // 2
            if self.bool_api(ranks, cars, mid) < True:
                lo = mid + 1
            else:
                hi = mid
        return lo

    # https://leetcode.com/problems/minimum-time-to-repair-cars/
