from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        result = 0
        hashmap = defaultdict(int)
        most_frequent = s[0]
        for c in s:
            hashmap[c] += 1
            if c != most_frequent and hashmap[c] > hashmap[most_frequent]:
                most_frequent = c
        l = 0
        count = 0
        for r in range(len(s)):
            if s[r] == most_frequent:
                count += 1
            window_size = r - l + 1
            while window_size > count + k:
                if s[l] == most_frequent:
                    count -= 1
                l += 1
                window_size -= 1
            result = max(result, window_size)
        return result