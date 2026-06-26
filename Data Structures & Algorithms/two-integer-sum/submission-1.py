class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        compliment = dict()
        for i, num in enumerate(nums):
            # T: 7 | N: 3 | D: 4
            diff = target - num
            if diff in compliment:
                return [compliment[diff], i]
            compliment[num] = i
        return []