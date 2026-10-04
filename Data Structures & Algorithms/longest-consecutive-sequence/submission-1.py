class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashmap = {}
        for i in range(len(nums)):
            for num in nums:
                if num - 1 not in hashmap:
                    hashmap[num] = 1
                else:
                    hashmap[num] = hashmap[num - 1] + 1
        if hashmap.values():
            return max(hashmap.values())
        return 0
