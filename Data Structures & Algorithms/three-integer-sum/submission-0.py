class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if nums[i] > 0:
                break
            target =  0 - nums[i]
            hashmap = {}
            for j in range(i + 1, len(nums)):
                diff = target - nums[j]
                if diff in hashmap:
                    if hashmap[diff] != -1:
                        result.append([nums[i], nums[hashmap[diff]], nums[j]])
                        hashmap[diff] = -1
                    else:
                        continue
                else:
                    hashmap[nums[j]] = j
        return result