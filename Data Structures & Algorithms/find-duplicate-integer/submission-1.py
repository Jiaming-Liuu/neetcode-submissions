class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast, slow = 0, 0
        fast = nums[nums[fast]]
        slow = nums[slow]
        while fast != slow:
            fast = nums[fast]
            fast = nums[fast]
            slow = nums[slow]
        
        new = 0
        while new != fast:
            new = nums[new]
            fast = nums[fast]
        return new