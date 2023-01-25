from typing import List

class Solution:
    def __init__(self) -> None:
        self.ans = []
        self.path = []
    
    def combine(self, n: int, k: int) -> List[List[int]]:

        def trackback(n, k, start):
            if len(self.path)==k: 
                self.ans.append(self.path[:])
                return None

            for i in range(start, n-(k-len(self.path))+1):
                self.path.append(i)
                trackback(n, k, i+1)
                self.path.pop()
        
        trackback(n, k, 1)
        return self.ans


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        path = []
        ans = []

        def traceback(k, n, startIndex):
            if len(path)==k:
                if sum(path)==n:
                    ans.append(path[:])
                return None
            
            for i in range(startIndex, 10-(k-len(path))+1):
                path.append(i)
                traceback(k, n, i+1)
                path.pop()
        traceback(k, n, 1)
        return ans

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ans = []
        path = []
        dic = {
            '2': "abc",
            '3':"def",
            '4':"ghi",
            '5':"jkl",
            '6':"mno",
            '7':"pqrs",
            '8':"tuv",
            '9':"wxyz"
        }

        def traceback(digits, depth):
            if depth>len(digits):
                ans.append("".join(path[:]))
                return

            digit = digits[depth-1]
            letters = dic[digit]
            for ch in letters:
                path.append(ch)
                traceback(digits, depth+1)
                path.pop()
        if digits=="":
            return []
        traceback(digits, 1)
        return ans
