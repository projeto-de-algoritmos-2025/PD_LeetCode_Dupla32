class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        arr = [1] + nums + [1]
        N = len(arr)
        dp = [[0] * N for _ in range(N)]

   
        for length in range(2, N):
        
            for i in range(N - length):
                j = i + length
                
                for k in range(i + 1, j):

                    current_gain = arr[i] * arr[k] * arr[j] + dp[i][k] + dp[k][j]
                    
                    dp[i][j] = max(dp[i][j], current_gain)
        

        return dp[0][N - 1]