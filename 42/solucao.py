class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)

        if n < 3:
            return 0

       
        left_max = [0] * n
        left_max[0] = height[0]
        for i in range(1, n):
            left_max[i] = max(left_max[i-1], height[i])

        right_max = [0] * n
        right_max[n-1] = height[n-1]
        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i+1], height[i])

        total_water = 0
        for i in range(n):
            
            water_level = min(left_max[i], right_max[i])
            
            trapped_at_current_bar = water_level - height[i]

            if trapped_at_current_bar > 0:
                total_water += trapped_at_current_bar

        return total_water