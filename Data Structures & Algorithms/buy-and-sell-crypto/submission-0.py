class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = 100
        highest = -1
        maxdiff = 0

        for i, p in enumerate(prices):
            if p < lowest:
                lowest = p
                subset = prices[i+1:]
                for q in subset:
                    if (diff := q-lowest) > maxdiff:
                        maxdiff = diff

        return maxdiff