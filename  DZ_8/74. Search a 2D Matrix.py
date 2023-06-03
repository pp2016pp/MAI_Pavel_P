class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        columns = len(matrix[0])  # столбцы
        rows = len(matrix)  # строки
        lo = 0
        hi = rows * columns - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            m = mid // columns
            n = mid % columns
            if matrix[m][n] == target:
                return True
            if matrix[m][n] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return False

    # https://leetcode.com/problems/search-a-2d-matrix/
