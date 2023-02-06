from typing import List, Optional

class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0]*(n+1)
        dp[0] = 1

        for i in range(1, n+1):
            for j in range(1, i):
                dp[i] += dp[j]*dp[i-j]
        
        return dp[-1]


def bag_problem(bag_size, weight, value) ->int:
    rows = len(weight)
    cols = bag_size+1

    dp = [[0 for _ in range(cols)] for _ in range(rows)]

    for i in range(rows):
        dp[i][0] = 0
    
    for j in range(1,cols):
        if j>=weight[0]:
            dp[0][j] = value[0]
    
    for j in range(1, cols):
        for i in range(1, rows):
            if j<weight[i]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight[i]]+value[i])
    print(dp)
    return dp[-1][-1]

def bag_problem2(bag_size, weight, value) -> int:
    rows = len(weight)
    cols = bag_size+1
    dp = [0 for _ in range(cols)]

    for j in range(cols):
        if j>=weight[0]: dp[j]=value[0]
    
    for i in range(rows):
        for j in range(cols-1, weight[i]-1, -1):
                dp[j] = max(dp[j], dp[j-weight[i]]+value[i])
    print(dp)
    return dp[-1]

if __name__=="__main__":
    bag_size = 4
    weight = [1, 3, 4]
    value = [15, 20, 30]
    # bag_problem(bag_size, weight, value)
    # bag_problem2(bag_size, weight, value)


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        summation = sum(nums)
        if summation%2==1: return False

        target = summation//2
        dp = [0]*(target+1)
        for i in range(len(nums)):
            for j in range(target, nums[i]-1, -1):
                dp[j] = max(dp[j], dp[j-nums[i]]+nums[i])
        
        return nums[target]==target