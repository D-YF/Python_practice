from typing import List

class Solution:
    def removeDuplicates(self, s: str) -> str:
        ans = []

        for item in s:
            if ans and ans[-1]==item:
                ans.pop()
            else:
                ans.append(item)
        
        return "".join(ans)

class Solution:
    def removeDuplicates(self, s: str) -> str:
        ans = list(s)
        slow, fast = 0, 0
        N = len(ans)

        while fast<N:
            ans[slow] = ans[fast]

            if slow>0 and ans[slow]==ans[slow-1]:
                slow -= 1
            else:
                slow += 1
            fast += 1

        return "".join(ans[:slow])


# s = "abbacee"
# sol = Solution()
# print(sol.removeDuplicates(s))


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        