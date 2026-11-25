from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        result = 0
        hashmap = defaultdict(int)
        l = 0
        most_freq = 0

        for r in range(len(s)):
            hashmap[s[r]] += 1
            most_freq = max(most_freq, hashmap[s[r]])

            while r - l + 1 > most_freq + k:
                hashmap[s[l]] -= 1
                l += 1
                    
            result = max(result, r - l + 1)
        return result