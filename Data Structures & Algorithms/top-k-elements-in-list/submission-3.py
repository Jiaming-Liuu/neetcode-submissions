from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
        reverse = defaultdict(list)
        for key in freq.keys():
            reverse[freq[key]].append(key)

        for i in range(len(nums), -1, -1):
            if i in reverse:
                for num in reverse[i]:
                    res.append(num)
        return res[:k]            