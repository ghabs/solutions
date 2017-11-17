class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_x = len(height) - 1
        i = 0
        max_area = 0
        while (i != max_x):
            if height[i] > height[max_x]:
                max_area = max(max_area, (max_x - i) * height[max_x])
                max_x = max_x - 1
            elif height[max_x] >= height[i]:
                max_area = max(max_area, (max_x - i) * height[i])
                i = i + 1
        return max_area
        
