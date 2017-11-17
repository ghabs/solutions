class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        p = nums[0]
        pp = nums[0]
        for i in nums[1:]:
            p = max(i, p + i)
            pp = max(p, pp)
        return pp
