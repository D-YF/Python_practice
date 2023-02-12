from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False]*(len(s)+1)
        dp[0] = True
        rows = len(wordDict)

        for j in range(len(s)+1):
            for i in range(rows):
                l = len(wordDict[i])
                if dp[j]==True:
                    continue
                if j>=l and dp[j-l] and s[j-l:j]==wordDict[i]:
                    dp[j]=True
        
        return dp[-1]

sol = Solution()
s = "leetcode"
wordDict = ["leet","code"]
sol.wordBreak(s, wordDict)