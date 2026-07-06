class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = -1
        for i, h in enumerate(heights):
            area = h
            left = i - 1
            right = i + 1
            while left >= 0 and heights[left] >= h:
                area += h
                left -= 1
            while right < len(heights) and heights[right] >= h:
                area += h
                right += 1
            maxArea = max(maxArea, area)
        return maxArea
            
        