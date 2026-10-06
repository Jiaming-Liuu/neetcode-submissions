class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for s in strs:
            ordered_s = "".join(sorted(s))
            if ordered_s in hashmap:
                hashmap[ordered_s].append(s)
            else:
                hashmap[ordered_s] = [s]
        return list(hashmap.values())