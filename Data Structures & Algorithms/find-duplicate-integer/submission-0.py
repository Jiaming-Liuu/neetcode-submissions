class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast, slow = 0, 0
        while 1:
            if nums[fast] == nums[slow] and fast != slow:
                break
            fast += 2
            slow += 1
            if fast >= len(nums):
                fast -= len(nums)
            if slow >= len(nums):
                slow -= len(nums)
        return nums[fast]