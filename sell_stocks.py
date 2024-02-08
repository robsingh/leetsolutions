"""
You are given an array prices, where prices[i] is the price of a given stock on the ith day. 
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the max profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
"""
from typing import List
class Solution:
    # def maxProfit(self, prices:List[int]) -> int:
    #     if not prices:
    #         return 0
    #     min_price = prices[0]
    #     max_profit = 0

    #     for price in prices:
    #         max_profit = max(max_profit, price - min_price)
    #         min_price = min(min_price, price)
        
    #     return max_profit
    def maxProfit(self, prices:List[int]) -> int:
        if not prices:
            return 0
        max_profit = 0
        # if the price is higher than the previous day, 
        # we can make profit by buying on the previous day
        # and selling on the current day.
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                max_profit += prices[i] - prices[i-1]

        return max_profit

# run time - complexity - O(n)
       
sol = Solution()
prices = [7,1,5,3,6,4]
print(sol.maxProfit(prices))