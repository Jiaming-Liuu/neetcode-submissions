class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result, cur_length = 0, 0
        l = 0
        seen = set()
        for r in range(len(s)):
            if s[r] not in seen:
                seen.add(s[r])
                cur_length += 1
                result = max(result, cur_length)
            else:
                while s[l] != s[r]:
                    seen.discard(s[l])
                    l += 1
                    cur_length -= 1
        return result