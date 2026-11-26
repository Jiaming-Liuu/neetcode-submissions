class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ''
        for string in strs:
            result += string
            result += '空'
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        cur = 0
        cur_str = ''
        while cur < len(s):
            if s[cur] == '空':
                result.append(cur_str)
                cur_str = ''
            else:
                cur_str += s[cur]
            cur += 1
        return result