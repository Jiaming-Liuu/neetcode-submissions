class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        reverse = {}
        for key in freq.keys():
            reverse[freq[key]] = key
        for i in range(len(nums), -1, -1):
            if i in reverse:
                res.append(reverse[i])
        return res[:k]            