class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        hashset = set()
        for num in nums:
            hashset.add(num)
        orderedlist = sorted(list(hashset))
        result = 1
        cur = 1
        for i in range(1, len(orderedlist)):
            if orderedlist[i - 1] + 1 == orderedlist[i]:
                cur += 1
                result = max(result, cur)
            else:
                cur = 1
        return result