class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        rank_dict = {}
        for rank in sorted(set(ranks)):
            rank_dict[rank] = len(rank_dict) + 1
        total_time = 0
        for rank in ranks:
            mechanic_rank = rank_dict[rank]
            time_for_one_car = mechanic_rank * (cars // len(ranks)) ** 2
            total_time += time_for_one_car
        return total_time