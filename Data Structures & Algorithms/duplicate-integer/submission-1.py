class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        myset = set(nums)
        return len(myset) != len(nums) 