class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        profit = 0
        for price in prices:
            if price > buy:
                profit = max(profit, price - buy)
            elif price < buy:
                buy = price
        return profit