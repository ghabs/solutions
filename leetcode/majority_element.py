class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hashmap = {}
        for i in nums:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1
        greatest = 0
        gind = 0
        for i in hashmap:
            if hashmap[i] > greatest:
                greatest = hashmap[i]
                gind = i
        return gind
            
