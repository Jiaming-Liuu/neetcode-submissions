class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        nums = []
        for array in matrix:
            nums += array
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return True
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return False