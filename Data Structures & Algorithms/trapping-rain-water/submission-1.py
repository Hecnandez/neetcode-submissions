class Solution:
    def trap(self, height: List[int]) -> int:
        prefix = [0] * len(height)
        suffix = [0] * len(height)
        maxLeft = height[0]
        maxRight = height[-1]
        water = 0

        for i in range(1, len(height) - 1):
            maxLeft = max(maxLeft, height[i])
            prefix[i] = maxLeft
        print(prefix)
        for i in range(len(height)-2, 0, -1):
            maxRight = max(maxRight, height[i])
            suffix[i] = maxRight
        print(suffix)
        for i in range(1, len(height)-1):
            water += min(prefix[i], suffix[i]) - height[i]

        return water