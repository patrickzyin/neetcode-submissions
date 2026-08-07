class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        priceMin = prices[0]
        maxProfit = 0
        for price in prices:
            if price < priceMin:
                priceMin = price
            profit = price - priceMin
            if profit > maxProfit:
                maxProfit = profit
        return maxProfit



        