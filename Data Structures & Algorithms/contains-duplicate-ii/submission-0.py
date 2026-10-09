class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = set(nums[:k])
        print(seen)
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