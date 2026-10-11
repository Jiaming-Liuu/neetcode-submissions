from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
        
        buckets = defaultdict(list)
        for key, value in freq.items():
            buckets[value].append(key)

        result = []
        for i in range(len(nums), -1, -1):
            if i in buckets:
                for value in buckets[i]:
                    result.append(value)
        
        return result[:k]