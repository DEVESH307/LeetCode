class Solution:
    def maxHeight(self, cuboids):
        # Step 1: normalize each cuboid
        for c in cuboids:
            c.sort()
        
        # Step 2: sort all cuboids
        cuboids.sort()
        
        n = len(cuboids)
        dp = [0] * n
        
        for i in range(n):
            dp[i] = cuboids[i][2]  # height
            
            for j in range(i):
                if (cuboids[j][0] <= cuboids[i][0] and
                    cuboids[j][1] <= cuboids[i][1] and
                    cuboids[j][2] <= cuboids[i][2]):
                    
                    dp[i] = max(dp[i], dp[j] + cuboids[i][2])
        
        return max(dp)