class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        comp = {}
        for ind, val in enumerate(nums):
            if val in comp:
                return [comp[val], ind]
            else:
                comp[target-val] = ind

        return []