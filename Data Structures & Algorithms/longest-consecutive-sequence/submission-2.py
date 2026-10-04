class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set()
        for num in nums:
            hashset.add(num)
        orderedlist = sorted(list(hashset))
        result = 0
        cur = 1
        for i in range(len(orderedlist)):
            if orderedlist[i - 1] + 1 == orderedlist[i]:
                cur += 1
                result = max(result, cur)
            else:
                cur = 1
        return result