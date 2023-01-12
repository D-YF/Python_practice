class Solution(object):
    def getKMParray(self, s):
        s = list(s)
        N = len(s)
        length = 0
        i = 1
        LPS = [0]*N

        while i < N:
            # This logic is hard to understand
            if s[i]==s[length]:
                length += 1
                LPS[i] = length
                i += 1
            else:
                if length==0:
                    LPS[i] = 0
                    i += 1
                else:
                    # pay attention to this line
                    length = LPS[length-1]
        return LPS

    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        LPS = self.getKMParray(s)
        N = len(LPS)
        max = LPS[-1]
        if max>=(N-max) and max%(N-max)==0:
            return True
        else:
            return False

s = "abac"
sol = Solution()
print(sol.getKMParray(s))
print(sol.repeatedSubstringPattern(s))