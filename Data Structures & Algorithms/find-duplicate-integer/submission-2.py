class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast, slow = 0, 0
        fast = nums[nums[fast]]
        slow = nums[slow]
        while fast != slow:
            fast = nums[nums[fast]]
            slow = nums[slow]
        print(fast, slow)

        new = 0
        while new != fast:
            fast = nums[fast]
            new = nums[new]
        return fast