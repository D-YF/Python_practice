from typing import List 

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        ans = []

        dic = {}
        for ch in s:
            dic[ch] = dic.get(ch, 0) + 1

        curdic = {s[0]:dic[s[0]]-1}
        count = 0
        for i in range(1, len(s)):
            count += 1

            if s[i] in curdic:
                curdic[s[i]] -= 1
            else:
                curdic[s[i]] = dic[s[i]]-1

            if sum(curdic.values())==0:
                ans.append(count)
                count = 0
                curdic.clear()
        
        return ans


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key= lambda x:x[0])

        ans = [intervals[0]]

        for i in range(1, len(intervals)):
            if intervals[i][0] <= ans[-1][1]:
                ans[-1][1] = max(intervals[i][1], ans[-1][1])
            else:
                ans.append(intervals[i])
        
        return ans


class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        ans = 0
        n = list(str(n))
        N = len(n)

        for i in range(N-1, 0, -1):
            if n[i] < n[i-1]:
                n[i:] = '9'*(len(n)-i)
                n[i-1] = str(int(n[i-1]) - 1)
        
        return int("".join(n))

