class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        l, r = 0, len(prices) - 1
        while l < r:
            if prices[l] > prices[l + 1]:
                l += 1
                result = max(result, prices[r] - prices[l])
            elif prices[r - 1] > prices[r]:
                r -= 1
                result = max(result, prices[r] - prices[l])
            else:
                break
        return result