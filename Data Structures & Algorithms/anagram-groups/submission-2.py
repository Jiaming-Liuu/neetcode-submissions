class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for s in strs:
            char_count = [0] * 26
            for c in s:
                char_count[ord(c) - ord('a')] += 1
            key = tuple(char_count)
            if key in hashmap:
                hashmap[key].append(s)
            else:
                hashmap[key] = [s]
        return list(hashmap.values())