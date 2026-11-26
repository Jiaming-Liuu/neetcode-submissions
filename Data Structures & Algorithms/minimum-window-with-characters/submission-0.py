from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_map = defaultdict(int)
        for c in t:
            t_map[c] += 1
        
        l = 0
        min_len = len(s) + 1
        min_start = 0
        s_map = defaultdict(int)
        for r in range(len(s)):
            s_map[s[r]] += 1
            while self.is_subset(t_map, s_map):
                if r - l + 1 < min_len:
                    min_len = r - l + 1
                    min_start = l

                s_map[s[l]] -= 1
                l += 1

        return s[min_start:min_start + min_len] if min_len <= len(s) else ''

    def is_subset(self, A, B):
        for key, value in A.items():
            if B.get(key, 0) < value:
                return False
        return True