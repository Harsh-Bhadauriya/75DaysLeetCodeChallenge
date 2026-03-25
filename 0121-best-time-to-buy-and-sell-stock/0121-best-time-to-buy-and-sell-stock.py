class Solution:
    def maxProfit(self, prices):
        mn = prices[0]
        ans = 0
        
        for i in range(1, len(prices)):
            if prices[i] < mn:
                mn = prices[i]
            else:
                diff = prices[i] - mn
                if diff > ans:
                    ans = diff
        
        return ans