class Solution:
    def findNumberOfLIS(self, nums: list[int]) -> int:
        n = len(nums)
        dp = [ [1,1] for _ in range(n) ]
        max_increasing = 1
        for i in range(n):
            current_max = 1
            running_count = 0
            for j in range(i):
                if nums[i] > nums[j]:
                    if dp[j][0] + 1 > current_max:
                        current_max = dp[j][0] + 1
                        running_count = 0
                    if dp[j][0] == current_max - 1:
                        running_count += dp[j][1]
            dp[i] = [current_max, max(running_count, dp[i][1])]
            max_increasing = max(max_increasing, current_max)
        return sum([x[1] for x in dp if x[0] == max_increasing])