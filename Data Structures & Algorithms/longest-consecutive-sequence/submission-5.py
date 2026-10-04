class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        hashset = set(nums)
        for num in hashset:
            if num - 1 not in hashset:
                cur_num = num
                cur_length = 1
                while cur_num + 1 in hashset:
                    cur_num += 1
                    cur_length += 1
                res = max(res, cur_length)
        return res