class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest_len = float('inf')
        shortest_index = 0;
        for i in range(len(strs)):
            shortest_len = min(len(strs[i]), shortest_len)
            if len(strs[i]) < shortest_len:
                shortest_len = len(strs[i])
                shortest_index = i
        if shortest_len == 0:
            return ""
        for j in range(shortest_len):
            cur_str = strs[0][0:j+1]
            for string in strs:
                if cur_str not in string:
                    return strs[0][0:j]
        return strs[i]
                