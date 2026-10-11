class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        sell = buy+1
        profit = 0
        while sell<len(prices):
            if prices[buy]<prices[sell]:
                profit = max(prices[sell]-prices[buy], profit)
            elif prices[buy]>prices[sell]:
                buy = sell
            sell +=1
        return profit
