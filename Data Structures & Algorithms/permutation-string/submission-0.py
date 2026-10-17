class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        list1 = [0] * 26
        for c in s1:
            list1[ord(c) - ord('a')] += 1

        list2 = [0] * 26
        for c in s2[:len(s1)]:
            list2[ord(c) - ord('a')] += 1
        
        if list1 == list2:
            return True
        
        for i in range(len(s1), len(s2)):
            list2[ord(s2[i]) - ord('a')] += 1
            list2[ord(s2[i - len(s1)]) - ord('a')] -= 1
            if list1 == list2:
                return True

        return False