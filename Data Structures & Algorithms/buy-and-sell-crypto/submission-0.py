class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        low_idx = 0 #this is my buy day
        for buy_i in range(1, len(prices)):
            if prices[low_idx] > prices[buy_i]: low_idx = buy_i 
            max_profit = max(max_profit, prices[buy_i] - prices[low_idx])
        return max_profit
