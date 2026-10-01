class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest_len = float('inf')
        for string in strs:
            shortest_len = min(len(string), shortest_len)
        for i in range(shortest_len):
            cur_str = strs[0][0:i+1]
            for string in strs:
                if cur_str not in string:
                    return strs[0][0:i]
                