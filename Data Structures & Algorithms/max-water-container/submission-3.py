class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        maxWater = 0
        while (i < j):
            water = (j - i) * min(heights[i], heights[j])
            maxWater = max(water, maxWater)
            if min(heights[i], heights[j]) == heights[i]:
                i += 1
            else:
                j -= 1

        return maxWater