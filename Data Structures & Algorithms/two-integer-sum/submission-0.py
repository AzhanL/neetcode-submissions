class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        compliment = dict()
        for i, num in enumerate(nums):
            # T: 7 | N: 3 | D: 4
            diff = target - num
            if num not in compliment.keys():
                compliment[diff] = i
            else:
                return [compliment[num], i]
        return []