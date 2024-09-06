class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price_so_far = float('inf')
        max_profit = 0
        for price in prices:
            min_price_so_far=min(min_price_so_far,price)
            max_profit = max(max_profit,price-min_price_so_far)
        return max_profit
            