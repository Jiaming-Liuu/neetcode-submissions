class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        hashset = set(nums)
        res = 1
        for num in hashset:
            if num - 1 not in hashset:
                cur_length = 1
                while num + 1 in hashset:
                    num += 1
                    cur_length += 1
                    res = max(res, cur_length)
        return res