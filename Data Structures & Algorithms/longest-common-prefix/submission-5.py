class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for i in range(1, len(strs[0]) + 1):
            cur_str = strs[0][:i]
            for string in strs:
                if len(string) < i or string[:i] != cur_str:
                    return string[:i - 1]
        return strs[0]