class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP, minB = 0, prices[0]
        for p in prices:
            maxP = max(maxP, p - minB)
            minB = min(minB, p)
        return maxP