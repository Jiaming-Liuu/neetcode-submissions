class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k == 0:
            return False
        seen = set(nums[:k])
        if len(seen) < k:
            return True
        l, r = 0, k
        while r < len(nums):
            if nums[r] in seen:
                return True
            else:
                seen.remove(nums[l])
                l += 1
                seen.add(nums[r])
                r += 1
        return False