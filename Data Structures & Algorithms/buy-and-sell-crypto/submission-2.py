class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = prices[0]
        l, r = 0, 0
        maxProfit = -100
        while r < len(prices):
            profit = prices[r] - prices[l]
            maxProfit = max(maxProfit, profit)
            lowest = min(lowest, prices[r])
            if prices[l] == lowest:
                r += 1
            else:
                l = r

        return max(0, maxProfit)
                