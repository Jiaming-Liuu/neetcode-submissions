from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_map = defaultdict(int)
        for c in t:
            t_map[c] += 1
        
        need, met = len(t_map), 0
        min_len = len(s) + 1
        min_start = 0
        s_map = defaultdict(int)
        l = 0
        for r in range(len(s)):
            s_map[s[r]] += 1
            if s[r] in t_map and s_map[s[r]] == t_map[s[r]]:
                met += 1
            
            while need == met:
                if r - l + 1 < min_len:
                    min_len = r - l + 1
                    min_start = l

                if s[l] in t_map and s_map[s[l]] == t_map[s[l]]:
                    met -= 1

                s_map[s[l]] -= 1
                l += 1
        
        return s[min_start:min_start + min_len] if min_len <= len(s) else ""