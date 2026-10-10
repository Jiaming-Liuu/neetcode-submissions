class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False
        up, down = 0, len(matrix) - 1
        while up <= down:
            mid = up + (down - up) // 2
            if matrix[mid][-1] == target:
                return True
            elif matrix[mid][-1] > target:
                down = mid - 1
            else:
                up = mid + 1
        row = up
        l, r = 0, len(matrix[0]) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        
        return False